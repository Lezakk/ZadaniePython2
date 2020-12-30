from abc import ABC, abstractclassmethod


class Samochod(ABC):
    def __init__(self, marka, model, waga, czesci=None):
        self.marka = marka
        self.model = model
        self.waga = waga
        self.czesci = czesci

    @abstractclassmethod
    def dodaj(self, nazwa, cena):
        self.czesci.append(str(nazwa), int(cena))

    @abstractclassmethod
    def wyswietl(self):
        print(czesci)

    def cena(self, nazwa):
        if nazwa not in self.czesci:
            print(nazwa + " - Nie ma takiej części!\nCena: 0")
        else:
            print("Cena %s: %s" % (nazwa, str(self.czesci[nazwa])))


class Osobowy(Samochod):
    def __init__(self, marka, model, waga, czesci=None):
        super().__init__(marka, model, waga, czesci)

    def wyswietl(self):
        print("Osobowy " + self.model, self.marka)
        if not self.czesci:
            print("Brak części.")
        else:
            print("Części:")
            for key, value in self.czesci.items():
                print(" " + key + ": " + str(value))

    def dodaj(self, nazwa, cena):
        self.czesci[str(nazwa)] = int(cena)


class Autobus(Samochod):
    def __init__(self, marka, model, waga, czesci=None):
        super().__init__(marka, model, waga, czesci)

    def wyswietl(self):
        print("Autobus " + self.model, self.marka)
        if not self.czesci:
            print("Brak części.")
        else:
            print("Części:")
            for key, value in self.czesci.items():
                print(" " + key + ": " + str(value))

    def dodaj(self, nazwa, cena):
        self.czesci[str(nazwa)] = int(cena)


Jelcz = Autobus("Jelcz", "M11", 9200, {"Opona": 400, "Zderzak": 300})
Jelcz.wyswietl()
Jelcz.cena("Opona")
Jelcz.dodaj("Wał korbowy", 350)
Jelcz.dodaj("Wał korbowy", 360)
Jelcz.cena("Wał korbowy")
Jelcz.cena("Kołpak")
Jelcz.wyswietl()
Corsa = Osobowy("Opel", "Corsa", 1200)
Corsa.wyswietl()
