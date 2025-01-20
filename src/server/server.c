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

    return EXIT_SUCCESS;
}