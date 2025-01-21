#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <netdb.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <errno.h>

// Just for test purposes

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

int main ( int argc, char** argv ){
    int fd;
    char buff[64];
    struct sockaddr_in addr;

    struct hostent* family_name;
    family_name = gethostbyname(argv[1]);

    if ( family_name == NULL ){
        fprintf(stderr, "Unknown host! Error: %s\n", strerror(errno));
        return EXIT_FAILURE;
    }

    fd = socket(PF_INET, SOCK_STREAM, 0);
    if ( fd < 0 ){
        fprintf(stderr, "Cannot create socket! Error: %s\n", strerror(errno));
        return EXIT_FAILURE;
    }
    
    addr.sin_family = AF_INET;
    addr.sin_port = htons(atoi(argv[2]));

    memcpy(&addr.sin_addr.s_addr, family_name->h_addr, family_name->h_length);

    if ( connect(fd, (struct sockaddr *) &addr, sizeof(addr)) ){
        fprintf(stderr, "Connect failed! Error: %s\n", strerror(errno));
        return EXIT_FAILURE;
    }
    

    printf("Wpisz numer indeksu: ");
    fgets(buff, sizeof(buff), stdin);
    write(fd, buff, 64);
    int i = __read(fd, buff, 64);
    printf("%s",buff);
    close(fd);

    return EXIT_SUCCESS;
}
