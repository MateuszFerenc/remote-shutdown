# sieci2_projekt_mferenc

  

# TODO opis

  

# Kompilacja i uruchomienie

Pliki z rozszerzeniem **.c** są kompilowane za pomocą polecenia **make**.<br>
Aby uruchomić pliki **.py** należy przygotować środowisko wirtualne:
``` ps
git clone --depth=1 https://git.cs.put.poznan.pl/inf151660/sieci2_projekt_mferenc

cd sieci2_projekt_mferenc
python3 -m venv .venv
.\.venv\Scripts\activate
pip3 install -r requirements.txt
python3 src\client\client.py
```