#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <netdb.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <sys/socket.h>
#include <sys/types.h>

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

int main ( int argc, char** argv ){
    socklen_t sl;
    int sfd, cfd, on = 1;
    struct sockaddr_in saddr, caddr;

    sfd = socket(PF_INET, SOCK_STREAM, 0);
    setsockopt(sfd, SOL_SOCKET, SO_REUSEADDR, (char*) &on, sizeof(on));
    saddr.sin_family = AF_INET;
    saddr.sin_port = htons(1234);
    saddr.sin_addr.s_addr = INADDR_ANY;
    
    bind(sfd, (struct sockaddr*) &saddr, sizeof(saddr));

    listen(sfd, 10);

    for(;;){
        sl = sizeof(caddr);
        cfd = accept(sfd, (struct sockaddr*) &caddr, &sl);
        printf("new connection: %s\n", inet_ntoa((struct in_addr) caddr.sin_addr));
        write(cfd, "Hello, World!\n", 15);
        close(cfd);
    }

    close(sfd);
    return EXIT_SUCCESS;
}