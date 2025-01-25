***
# Projekt zdalnego wyłączania komputerów
## Opis projektu
Wykorzystując połączenie TCP, aplikacja klienta ustala adresy komputerów obsługujących usługę (mających włączoną aplikację serwera).<br><br>
Aplikacja klienta (wyposażona w GUI), zestawia połączenia do serwerów pod wskazane adresy IP (lista lub zakres).<br>
Komputery z aktywną usługą są wyświetlone w aplikacji.<br>
Usługa wyłączenia obejmuje:
- Wyłączenie wszystkich komputerów
- Wyłączenia grupy komputerów
- Wyłaczenia wybranego komputera
  
***
# Kompilacja i uruchomienie

Pliki z rozszerzeniem **.c** są kompilowane za pomocą polecenia **make**.<br><br>
Aby uruchomić pliki **.py** należy przygotować środowisko wirtualne:
``` bash
git clone --depth=1 https://git.cs.put.poznan.pl/inf151660/sieci2_projekt_mferenc.git

cd sieci2_projekt_mferenc
python3 -m venv .venv
.venv\Scripts\activate
pip3 install -r requirements.txt

# uruchomienie klienta (bez SSL)
python3 src\client\client.py

# ALBO uruchomienie klienta (z SSL)
python3 src\client\client_ssl.py

# kompilacja i uruchomienie serwera (domyślnie bez SSL)
make run

# ALBO kompilacja i uruchomienie serwera (z SSL)
make run_ssl

# w razie potrzeby wygenerowania certyfikatów użyć
make gen_cert

# w razie potrzeby konwersji plików .ui na .py (GUI)
make gen_ui
```
***
# Używany protokół komunikacyjny
Wybrany został protokół TCP, ponieważ zapewnia on:
- możliwość wysyłania konkretnych sekwencji danych (wtedy gdy kolejność transmisji ma znaczenie)
- retransmisję w przypadku błędów
- dostarczenie danych jest gwarantowane
- sprawdzanie poprawności odebrnaych danych

***
# Struktura plików

``` ps
../sieci2_projekt_mferenc/
├── .gitignore
├── Makefile                        # plik z regułami dla programu Make
├── README.md
├── requirements.txt                # plik zawierający informacje dla menadżera pakietów Pythona (pip)
└── src
    ├── client
    │   ├── author_image.png
    │   ├── author_ui.py            # plik GUI przetłumaczony na j. Python (okno informacji o autorze)
    │   ├── author_ui.ui            # plik GUI w formacie XML (okno informacji o autorze)
    │   ├── __client_base.py        # bazowa klasa aplikacji (backend)
    │   ├── client.py               # klient bez SSL
    │   ├── client_ssl.py           # klient z SSL
    │   ├── documentation.py        # plik GUI przetłumaczony na j. Python (okno dokumentacji)
    │   ├── documentation.ui        # plik GUI w formacie XML (okno dokumentacji)
    │   ├── main_ui.py              # plik GUI przetłumaczony na j. Python (główne okno aplikacji)
    │   └── main_ui.ui              # plik GUI w formacie XML (główne okno aplikacji)
    └── server
        ├── server.c                # serwer bez SSL
        └── server_ssl.c            # serwer z SSL
```

# TODO
Konieczne:
- [x] Podstawowa implementacja klienta
- [x] Podstawowa implementacja serwera
- [x] Przygotowanie Makefile
- [x] Przygotowanie dokumentacji (README.md)
- [x] Podstawowy protokół komunikacji
- [x] Pełen protokół komunikacji
- [x] Bezpieczny protokół komunikacji (OpenSSL) **zaimplementowany nie można przetestować**
- [x] Zaimplementować wyłaczanie komputera przez aplikację serwera
- [x] Przygotować wstępne GUI (Qt5)
- [x] Pełne GUI klienta (Qt5)
- [x] Funkcjonalne GUI klienta (Qt5)
- [x] Automatyczna konwersja (w Makefile) z **.ui** do **.py** (Qt5)

Opcjonalne:
- [x] Aplikacje klienta (z i bez SSLu) dziedziczą z klasy nadrzędnej (__clientbase.py) [dzięki temu kod się nie powtarza]
- [ ] Dodać tooltipy
- [ ] Dodać zmianę języków
- [x] Dodać wyświetlanie dokumentacji
- [ ] Naprawić problem ze skalowaniem interfejsu **wymagane dalsze działania**