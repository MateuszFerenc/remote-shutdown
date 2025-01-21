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

/*
Kroki budowy serwera:
1. Utworzenie gniazda
2. Konfiguracja gniazda
3. inicjalizacja struktury adresowej
4. Zbindowanie struktury adresowej do gniazda
5. otwarcie listenera na gnieżdzie
6. Akceptacja połączenia
7. Komunikacja
8. Zakończenie połączenia
9. Przejdź do 6

*/ 

#define SERVER_PORT	21037U

int __read(int fd, char * buf, int size){
	int sum = 0, rc = 0;
	do {
		rc = read(fd, buf, size);
		if ( rc < 0 ) return rc;
		buf += rc;
		size -= rc;
		sum += rc;
	} while ( ( *buf - 1 ) != '\n' );
	return sum;
}

int main ( void ){
    int sfd, cfd, rc, fdmax, on = 1, fda, slt, i;
    fd_set mask, rmask, wmask, author, hostname;
    struct sockaddr_in saddr, caddr;
    static struct timeval timeout;
    char buff[64];
    int read_len;

    sfd = socket(PF_INET, SOCK_STREAM, 0);
    if ( sfd < 0 ){
        fprintf(stderr, "Cannot create socket! Error: %s\n", strerror(errno));
        return EXIT_FAILURE;
    }


    if ( setsockopt(sfd, SOL_SOCKET, SO_REUSEADDR, (char*) &on, sizeof(on)) ){
        fprintf(stderr, "setsockopt() failed! Error: %s\n", strerror(errno));
        close(sfd);
        return EXIT_FAILURE;
    }

    if ( ioctl(sfd, FIONBIO, (char*) &on) ){
        fprintf(stderr, "ioctl() failed! Error: %s\n", strerror(errno));
        close(sfd);
        return EXIT_FAILURE;
    }

    saddr.sin_family = AF_INET;
    saddr.sin_port = htons(SERVER_PORT);
    saddr.sin_addr.s_addr = INADDR_ANY;
    
    if ( bind(sfd, (struct sockaddr*) &saddr, sizeof(saddr)) ){
        fprintf(stderr, "bind() failed! Error: %s\n", strerror(errno));
        close(sfd);
        return EXIT_FAILURE;
    }

    if ( listen(sfd, 10) ){
        fprintf(stderr, "listen() failed! Error: %s\n", strerror(errno));
        close(sfd);
        return EXIT_FAILURE;
    }

    FD_ZERO(&mask);
    FD_ZERO(&rmask);
    FD_ZERO(&wmask);
    fdmax = sfd;

    timeout.tv_sec  = 3 * 60;
    timeout.tv_usec = 0;

    for(;;){
    	FD_SET(sfd, &rmask);
    	wmask = mask;
    	
    	rc = select(fdmax + 1, &rmask, &wmask, (fd_set *)0, &timeout);
    	
    	if ( ! rc ){
    		fprintf(stderr, "Select() timed out\n");
    		continue;
    	}
    	
    	fda = rc;
    	
    	if ( FD_ISSET(sfd, &rmask) ) {
    		fda -= 1;
    		slt = sizeof(caddr);

    		cfd = accept(sfd, (struct sockaddr *) &caddr, (socklen_t *)&slt);
            printf("new connection from %s:%d\n", inet_ntoa((struct in_addr)caddr.sin_addr), ntohs(caddr.sin_port));

    		FD_SET(cfd, &mask);
    		if ( cfd > fdmax ) fdmax = cfd;
    	}
    	
    	for ( i = sfd + 1; i <= fdmax && fda > 0; i++){
    		if ( FD_ISSET(i, &wmask) ){
				printf("write\n");
    			fda -= 1;
    			if ( FD_ISSET(i, &author) ){
    				write(cfd, "Mateusz Ferenc\n", 14);
    				FD_CLR(i, &author);
    			} else 
    			if ( FD_ISSET(i, &hostname) ){
                    char hn[_SC_HOST_NAME_MAX+1];
                    gethostname(hn, _SC_HOST_NAME_MAX+1);
                    int len = sprintf(buff, "%s\n", hn);
    				write(cfd, buff, len);
    				FD_CLR(i, &hostname);
    			} else
    				write(cfd, "Unknown\n", 8);
    			
    			close(i);
    			FD_CLR(i, &mask);
    			if ( i == fdmax )
    				while ( fdmax > sfd && !FD_ISSET(fdmax, &mask) )
    					fdmax -= 1;
				printf("out1\n");
    		} else
    		if ( FD_ISSET(i, &rmask) ) {
				printf("read\n");
    			fda -= 1;
    			read_len = __read(cfd, buff, 64);
                if(read_len){
                	if(strncmp("author", buff, 6) == 0)
			        	FD_SET(i, &author);
                    else 
			    	if(strncmp("hostname", buff, 8) == 0)
			    		FD_SET(i, &hostname);
                }
                printf("buff = %s\n", buff);
    			close(i);
    			FD_CLR(i, &mask);
    			if ( i == fdmax )
    				while ( fdmax > sfd && !FD_ISSET(fdmax, &mask) )
    					fdmax -= 1;
				printf("out2\n");
    		}
    	}
    }

    close(sfd);

    return EXIT_SUCCESS;
}