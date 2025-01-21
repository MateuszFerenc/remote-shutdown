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
  

# Kompilacja i uruchomienie

Pliki z rozszerzeniem **.c** są kompilowane za pomocą polecenia **make**.<br><br>
Aby uruchomić pliki **.py** należy przygotować środowisko wirtualne:
``` ps
git clone --depth=1 https://git.cs.put.poznan.pl/inf151660/sieci2_projekt_mferenc.git

cd sieci2_projekt_mferenc
python3 -m venv .venv
. .venv\Scripts\activate
pip3 install -r requirements.txt
python3 src\client\client.py
```

# TODO
- [&check;] Podstawowa implementacja klienta
- [&check;] Podstawowa implementacja serwera
- [&check;] Przygotowanie Makefile
- [ ] Przygotowanie dokumentacji
- [ ] Podstawowy protokół komunikacji
- [ ] Zaimplementować wyłaczanie komputera przez aplikację serwera
- [&check;] Przygotować wstępne GUI (Qt5)
- [ ] pełne GUI klienta (Qt5)
- [ ] funkcjonalne GUI klienta (Qt5)
- [ ] automatyczna konwersja (w Makefile) z **.ui** do **.py** (Qt5)