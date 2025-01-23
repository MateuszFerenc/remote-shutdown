#define _POSIX_C_SOURCE 200112L
#define _XOPEN_SOURCE 500U

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <netdb.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <sys/ioctl.h>
#include <sys/select.h>

#include <errno.h>
#include <limits.h>
#include <fcntl.h>

#include <unistd.h>
#include <linux/reboot.h>
#include <sys/reboot.h>


int __shutdown( void ) {
    sync();
    setuid(0);
    return reboot(LINUX_REBOOT_CMD_POWER_OFF);
}

#define SERVER_PORT	21037U
#define REC_BUFF_SIZE	64

int __read(int fd, char *buf, unsigned int size){
	int length = 0, received = 0;
	do {
		received = recv(fd, buf, size, 0);
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

int main ( void ){
    int server_fd, client_fd, fd_max, fda, i;
    fd_set mask, rmask, wmask, author, hostname;
    struct sockaddr_in server_addr_struct, client_addr_struct;
	socklen_t socket_length = sizeof(client_addr_struct);
	static struct timeval timeout;

    char buff[ REC_BUFF_SIZE ];
    int read_len;

	memset(&server_addr_struct, 0, sizeof server_addr_struct);
	memset(&client_addr_struct, 0, sizeof client_addr_struct);

    if ( ( server_fd = socket(PF_INET, SOCK_STREAM, IPPROTO_TCP) ) < 0 ){
        fprintf(stderr, "Cannot create socket! Error: %s\n", strerror(errno));
        return EXIT_FAILURE;
    }


    if ( setsockopt(server_fd, SOL_SOCKET, SO_REUSEADDR, &(int){1}, sizeof(int)) < 0 ){
        fprintf(stderr, "setsockopt() failed! Error: %s\n", strerror(errno));
        close(server_fd);
        return EXIT_FAILURE;
    }

	makenonblocking(server_fd);

    server_addr_struct.sin_family = AF_INET;
    server_addr_struct.sin_port = htons(SERVER_PORT);
    server_addr_struct.sin_addr.s_addr = INADDR_ANY;
    
    if ( bind(server_fd, (struct sockaddr*) &server_addr_struct, sizeof(server_addr_struct)) < 0 ){
        fprintf(stderr, "bind() failed! Error: %s\n", strerror(errno));
        close(server_fd);
        return EXIT_FAILURE;
    }

    if ( listen(server_fd, 10) < 0 ){
        fprintf(stderr, "listen() failed! Error: %s\n", strerror(errno));
        close(server_fd);
        return EXIT_FAILURE;
    }

	printf("Listening on port %d...\n", SERVER_PORT);

    FD_ZERO(&mask);
    FD_ZERO(&rmask);
    FD_ZERO(&wmask);
	FD_ZERO(&author);
    FD_ZERO(&hostname);
    fd_max = server_fd;

    for(;;){
    	FD_SET(server_fd, &rmask);
    	wmask = mask;

		timeout.tv_sec  = 3 * 60;
    	timeout.tv_usec = 0;
    	
		fda = select( fd_max + 1, &rmask, &wmask, (fd_set *)0, &timeout );

		if ( fda == 0)
			continue;
		else
    	if ( fda < 0 ){
    		fprintf(stderr, "select() failed! Error: %s\n", strerror(errno));
    		close(server_fd);
			return EXIT_FAILURE;
    	}
    	
    	if ( FD_ISSET(server_fd, &rmask) ) {
    		fda -= 1;

    		client_fd = accept(server_fd, (struct sockaddr *) &client_addr_struct, &socket_length);
			makenonblocking(client_fd);
            printf("Got connection from %s:%d\n", inet_ntoa((struct in_addr)client_addr_struct.sin_addr), ntohs(client_addr_struct.sin_port));

    		FD_SET(client_fd, &mask);
    		if ( client_fd > fd_max ) fd_max = client_fd;
    	}
    	
    	for ( i = server_fd + 1; i <= fd_max && fda > 0; i++){
    		if ( FD_ISSET(i, &wmask) ){
    			fda -= 1;
    			if ( FD_ISSET(i, &author) ){
    				write(i, "HI CLIENT", 9);
    				FD_CLR(i, &author);
    			} else 
    			if ( FD_ISSET(i, &hostname) ){
                    char hn[HOST_NAME_MAX + 1];
                    gethostname(hn, HOST_NAME_MAX + 1);
    				write(i, hn, HOST_NAME_MAX);
    				FD_CLR(i, &hostname);
    			} else
    				write(i, "HI CLIENT", 9);
    			
    			//close(i);
    			FD_CLR(i, &mask);
    			if ( i == fd_max ){
					while ( fd_max > server_fd && !FD_ISSET(fd_max, &mask) )
    					fd_max -= 1;
				}
    		} else
    		if ( FD_ISSET(i, &rmask) ) {
    			fda -= 1;

				memset(buff, 0, REC_BUFF_SIZE);
    			read_len = __read( i, buff, REC_BUFF_SIZE );
				printf("%s", buff);
                if(read_len){
                	if(strncmp("HI SERVER", buff, 9) == 0)
			        	FD_SET(i, &author);
                    else 
			    	if(strncmp("hostname", buff, 8) == 0)
			    		FD_SET(i, &hostname);
					else
					if(strncmp("CLOSE", buff, 8) == 0){
						close(i);
						FD_CLR(i, &mask);
					}
                }
    			// TODO when we need to close connection with client
				//close(i);
				FD_CLR(i, &mask);
    			if ( i == fd_max ){
					while ( fd_max > server_fd && !FD_ISSET(fd_max, &mask) )
    					fd_max -= 1;
				}
    		}
    	}
    }

    close(server_fd);

    return EXIT_SUCCESS;
}