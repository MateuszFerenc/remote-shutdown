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
``` ps
git clone --depth=1 https://git.cs.put.poznan.pl/inf151660/sieci2_projekt_mferenc.git

cd sieci2_projekt_mferenc
python3 -m venv .venv
. .venv\Scripts\activate
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
```
../sieci2_projekt_mferenc/
├── .gitignore
├── Makefile
├── README.md
├── requirements.txt
└── src
    ├── client
    │   ├── author_image.png
    │   ├── author_ui.py
    │   ├── author_ui.ui
    │   ├── client.py
    │   ├── client_ssl.py
    │   ├── main_ui.py
    │   └── main_ui.ui
    └── server
        ├── server.c
        └── server_ssl.c
```

# TODO
Konieczne:
- [x] Podstawowa implementacja klienta
- [x] Podstawowa implementacja serwera
- [x] Przygotowanie Makefile
- [ ] Przygotowanie dokumentacji (README.md)
- [x] Podstawowy protokół komunikacji
- [x] Pełen protokół komunikacji
- [x] Bezpieczny protokół komunikacji (OpenSSL) [**nie można przetestować**]
- [x] Zaimplementować wyłaczanie komputera przez aplikację serwera
- [x] Przygotować wstępne GUI (Qt5)
- [x] pełne GUI klienta (Qt5)
- [x] funkcjonalne GUI klienta (Qt5)
- [x] automatyczna konwersja (w Makefile) z **.ui** do **.py** (Qt5)

Opcjonalne:
- [ ] Dodać tooltipy
- [ ] Dodać zmianę języków
- [ ] Dodać wyświetlanie dokumentacji