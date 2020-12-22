from abc import ABC, abstractclassmethod


class Samochod(ABC):
    def __init__(self, marka, model, waga, czesci):
        self.marka = marka
        self.model = model
        self.waga = waga
        self.czesci = {}


        @abstractclassmethod
        def dodaj(self, nazwa, cena):
            self.czesci.append(str(nazwa), int(cena))

        @abstractclassmethod
        def wyswietl(self):
            print(czesci)

        def cena(self, nazwa):
            if nazwa not in czesci:
                print("Nie ma takiej części!\nCena: 0")
            print("Cena: "czesci[nazwa])


class Osobowy(Samochod):
    def __init__(self, marka, model, waga, czesci):
        super().__init__(marka, model, waga, czesci)

    def wyswietl(self):
        print("Sklep samochod " + self.model, self.marka)
        if len(self.czesci) == 0:
            print("Nie wprowadzono części wyposażnia.")
        else:
            print(self.czesci)

    def dodaj(self, nazwa, cena):
        self.czesci.append(str(nazwa), int(cena))


class Autobus(Samochod):
    def __init__(self, marka, model, waga, czesci):
        super().__init__(marka, model, waga, czesci)

    def wyswietl(self):
        print("Autobus " + self.model, self.marka)
        if len(self.czesci) == 0:
            print("Brak części.")
        else:
            print(self.czesci)

    def dodaj(self, nazwa, cena):
        self.czesci.append(str(nazwa), int(cena))


