#define _POSIX_C_SOURCE 200112L
#define _XOPEN_SOURCE 500U

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <sys/socket.h>
#include <sys/select.h>

#include <errno.h>
#include <limits.h>

#include <sys/epoll.h>
#include <fcntl.h>

#include <unistd.h>
#include <linux/reboot.h>
#include <sys/reboot.h>

#include <openssl/bio.h>
#include <openssl/ssl.h>
#include <openssl/err.h>


#define SERVER_PORT	21037U
#define REC_BUFF_SIZE	96
#define MAX_EPOLL_EVENTS    1
#define CERT_FILE "cert.pem"
#define KEY_FILE "key.pem"

int __shutdown( void ) {
    sync();
    setuid(0);
    return reboot(LINUX_REBOOT_CMD_POWER_OFF);
}

int __read(SSL *fd, char *buf, unsigned int size){
	int length = 0, received = 0;
	do {
		received = SSL_read(fd, buf, size);
		if ( received < 0 ) return received;
		buf += received;
		size -= received;
		length += received;
	} while ( received > 0 );	// ( *buf - 1 ) != '\0'

	return length;
}

void makenonblocking(int fd){
	int flags = fcntl(fd, F_GETFL, 0);
	if ( flags < 0 )
        fprintf(stderr, "fcntl() failed! Error: %s\n", strerror(errno));
	if ( fcntl(fd, F_SETFL, flags | O_NONBLOCK) < 0 )
        fprintf(stderr, "fcntl() failed! Error: %s\n", strerror(errno));
}

SSL_CTX* create_SSL_context( void ){
    // Create SSL context [server side SSLv23_server_method()]
    SSL_CTX *ssl_context = SSL_CTX_new( SSLv23_server_method() );
    if ( ssl_context == NULL ){
        ERR_print_errors_fp(stderr);
        return NULL;
    }
    return ssl_context;
}

int configure_SSL_context(SSL_CTX *ctx) {
    SSL_CTX_set_options(ctx, SSL_OP_NO_SSLv2);
    if (SSL_CTX_use_certificate_file(ctx, CERT_FILE, SSL_FILETYPE_PEM) <= 0 ||
        SSL_CTX_use_PrivateKey_file(ctx, KEY_FILE, SSL_FILETYPE_PEM) <= 0) {
        ERR_print_errors_fp(stderr);
        return -1;
    }
    return 0;
}

int main ( void ){
    struct epoll_event event, current_event, events[MAX_EPOLL_EVENTS];
    struct sockaddr_in server_addr_struct, client_addr_struct;
    socklen_t socket_length = sizeof(client_addr_struct);
    int serverFd, epollFd, epoll_ReadyFd, active_client, clientFd;
    fd_set greeting_set, hostname_set, test_set, kill_set, shutdown_set;

    SSL_CTX *ssl_context;
    SSL *cSSL;

    char buff[ REC_BUFF_SIZE ];
    int read_len;

	memset(&server_addr_struct, 0, sizeof server_addr_struct);
	memset(&client_addr_struct, 0, sizeof client_addr_struct);

    // Initialise SSL
    SSL_load_error_strings();
    OpenSSL_add_all_algorithms();
    // ERR_print_errors(stderr);

    if ( SSL_library_init() < 0 ){
        fprintf(stderr, "SSL_library_init() failed! Error: %s\n", strerror(errno));
        return EXIT_FAILURE;
    }

    // Socket creation
    if ( ( serverFd = socket(PF_INET, SOCK_STREAM, IPPROTO_TCP) ) < 0 ){
        fprintf(stderr, "Cannot create socket! Error: %s\n", strerror(errno));
        return EXIT_FAILURE;
    }

    // Setting socket options (PORT can be reused immediately)
    if ( setsockopt(serverFd, SOL_SOCKET, SO_REUSEADDR, &(int){1}, sizeof(int)) < 0 ){
        fprintf(stderr, "setsockopt() failed! Error: %s\n", strerror(errno));
        close(serverFd);
        return EXIT_FAILURE;
    }

    // Make server I/O operations nonblocking
	makenonblocking(serverFd);

    // Initialize addres structure
    server_addr_struct.sin_family = AF_INET;
    server_addr_struct.sin_port = htons(SERVER_PORT);
    server_addr_struct.sin_addr.s_addr = INADDR_ANY;
    
    if ( bind(serverFd, (struct sockaddr*) &server_addr_struct, sizeof(server_addr_struct)) < 0 ){
        fprintf(stderr, "bind() failed! Error: %s\n", strerror(errno));
        close(serverFd);
        return EXIT_FAILURE;
    }

    if ( listen(serverFd, 10) < 0 ){
        fprintf(stderr, "listen() failed! Error: %s\n", strerror(errno));
        close(serverFd);
        return EXIT_FAILURE;
    }

	printf("Listening on port %d...\n", SERVER_PORT);

    if ( ( epollFd = epoll_create1(EPOLL_CLOEXEC) ) < 0 ){
        fprintf(stderr, "epoll_create1() failed! Error: %s\n", strerror(errno));
        close(serverFd);
        return EXIT_FAILURE;
    }

    event.events = EPOLLIN;
    event.data.fd = serverFd;

    if ( epoll_ctl( epollFd, EPOLL_CTL_ADD, serverFd, &event ) ){
        fprintf(stderr, "epoll_ctl() failed! Error: %s\n", strerror(errno));
        close(serverFd);
        return EXIT_FAILURE;
    }

    if ( ( ssl_context = create_SSL_context() ) == NULL ){
        fprintf(stderr, "create_SSL_context() failed!\n" );
        close(serverFd);
        return EXIT_FAILURE;
    }
    
    if ( ( configure_SSL_context(ssl_context) ) == -1 ){
        fprintf(stderr, "configure_SSL_context() failed!\n" );
        close(serverFd);
        SSL_CTX_free(ssl_context);
        return EXIT_FAILURE;
    }

    FD_ZERO(&greeting_set);
    FD_ZERO(&hostname_set);
    FD_ZERO(&test_set);
    FD_ZERO(&kill_set);
    FD_ZERO(&shutdown_set);

	int alive = 1;
    while(alive){
        epoll_ReadyFd = epoll_wait( epollFd, events, MAX_EPOLL_EVENTS, -1);

        if ( epoll_ReadyFd == -1 ){
            fprintf(stderr, "epoll() failed! Error: %s\n", strerror(errno));
            alive = 0;
            break;
        } else if( epoll_ReadyFd == 0 ){
            fprintf(stderr, "epoll() Timeout!\n");
            alive = 0;
            break;
        }

        for ( active_client = 0; active_client < epoll_ReadyFd; active_client++){
            current_event = events[ active_client ];
            cSSL = (SSL *)current_event.data.ptr;

            if ( current_event.data.fd == serverFd ){
                clientFd = accept( serverFd, (struct sockaddr *) &client_addr_struct, &socket_length );

                if ( clientFd == -1 ){
                    fprintf( stderr, "accept() failed! Error: %s\n", strerror(errno) );
					alive = 0;
                    break;
                }

			    makenonblocking(clientFd);

                printf( "Got connection from %s:%d\n", inet_ntoa((struct in_addr)client_addr_struct.sin_addr), ntohs(client_addr_struct.sin_port) );

                if ( ( cSSL = SSL_new( ssl_context ) ) == NULL ){
                    fprintf( stderr, "SSL_new() failed! Error: %s\n", strerror(errno) );
                    alive = 0;
                    break;
                }

                SSL_set_fd( cSSL, clientFd );

                if ( SSL_accept( cSSL ) <= 0 ){
                    // fprintf( stderr, "SSL_accept() failed! Error:\n" );
                    fprintf( stderr, "SSL_accept() failed! Error: %s\n", strerror(errno) );
                    ERR_print_errors_fp( stderr );
                    close( clientFd );
                } else {
                    printf( "SSL established for %s:%d\n", inet_ntoa((struct in_addr)client_addr_struct.sin_addr), ntohs(client_addr_struct.sin_port) );
                    event.data.ptr = cSSL;
                    event.data.fd = clientFd;
                    event.events = EPOLLIN | EPOLLONESHOT | EPOLLET;
                    epoll_ctl( epollFd, EPOLL_CTL_ADD, clientFd, &event );
                }
            } else
            if ( current_event.events & EPOLLIN ){
                memset( buff, 0, REC_BUFF_SIZE );
    			read_len = __read( cSSL, buff, REC_BUFF_SIZE );

                if(read_len){
                	if ( strncmp("HI SERVER", buff, 9) == 0 )
			        	FD_SET( current_event.data.fd, &greeting_set );
                    else 
			    	if ( strncmp("HOSTNAME", buff, 8) == 0 )
			    		FD_SET( current_event.data.fd, &hostname_set );
					else
					if ( strncmp("KILL", buff, 5) == 0 )
			    		FD_SET( current_event.data.fd, &kill_set );
					else
					if ( strncmp("SHUTDOWN", buff, 8) == 0 )
			    		FD_SET( current_event.data.fd, &shutdown_set );
					else
					if ( strncmp("TEST", buff, 8) == 0 )
			    		FD_SET( current_event.data.fd, &test_set );
					else {
					// if(strncmp("CLOSE", buff, 5) == 0){
                        getpeername( current_event.data.fd, (struct sockaddr *) &client_addr_struct, &socket_length );
						epoll_ctl( epollFd, EPOLL_CTL_DEL, current_event.data.fd, NULL );
                        close( current_event.data.fd );
                        SSL_free( cSSL );
                        SSL_shutdown( cSSL );
                        current_event.data.fd = -1;
                        printf( "Closed connection with %s:%d\n", inet_ntoa((struct in_addr)client_addr_struct.sin_addr), ntohs(client_addr_struct.sin_port) );
					}
                }
                
                if ( current_event.data.fd > 0 ){
                    event.events = EPOLLOUT | EPOLLONESHOT | EPOLLET;
                    epoll_ctl( epollFd, EPOLL_CTL_MOD, current_event.data.fd, &event );
                }
            } else
            if ( current_event.events & EPOLLOUT ){
                if ( FD_ISSET( current_event.data.fd, &greeting_set ) ){
    				SSL_write( cSSL, "HI CLIENT", 9 );
    				FD_CLR( current_event.data.fd, &greeting_set );
    			} else 
				if ( FD_ISSET( current_event.data.fd, &test_set ) ){
    				SSL_write( cSSL, "OK", 2 );
    				FD_CLR( current_event.data.fd, &test_set );
    			} else 
				if ( FD_ISSET( current_event.data.fd, &shutdown_set ) ){
    				SSL_write( cSSL, "OK", 2 );
    				FD_CLR( current_event.data.fd, &shutdown_set );
					if (__shutdown() == 0)
						printf("Shutting down...");
					else {
						fprintf( stderr, "shutdown() failed! Error: %s\n", strerror(errno) );
						alive = 0;
                    	break;
					}
    			} else 
				if ( FD_ISSET( current_event.data.fd, &kill_set ) ){
    				SSL_write( cSSL, "OK", 2 );
					alive = 0;
    				break;
    			} else 
    			if ( FD_ISSET( current_event.data.fd, &hostname_set ) ){
					memset( &buff, 0, HOST_NAME_MAX );
                    gethostname( buff, HOST_NAME_MAX + 1 );
    				SSL_write( cSSL, buff, HOST_NAME_MAX );
    				FD_CLR( current_event.data.fd, &hostname_set );
    			} 
				
                event.events = EPOLLIN | EPOLLONESHOT | EPOLLET;
                epoll_ctl( epollFd, EPOLL_CTL_MOD, current_event.data.fd, &event );
            }
        }
    }

    close(epollFd);
    close(serverFd);
    SSL_CTX_free(ssl_context);
    ERR_free_strings();
    EVP_cleanup();

    return EXIT_SUCCESS;
}