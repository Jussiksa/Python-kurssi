class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi

    def tulosta_tiedot(self):
        print(f"Julkaisu: {self.nimi}")


class Lehti(Julkaisu):
    def __init__(self, nimi, paatoimittaja):
        super().__init__(nimi)
        self.paatoimittaja = paatoimittaja

    def tulosta_tiedot(self):
        print(f"Lehti: {self.nimi}")
        print(f"Päätoimittaja: {self.paatoimittaja}\n")


class Kirja(Julkaisu):
    def __init__(self, nimi, kirjailija, sivumaara):
        super().__init__(nimi)
        self.kirjailija = kirjailija
        self.sivumaara = sivumaara

    def tulosta_tiedot(self):
        print(f"Kirja: {self.nimi}")
        print(f"Kirjailija: {self.kirjailija}")
        print(f"Sivumaara: {self.sivumaara} sivua\n")


# Pääohjelma
if __name__ == "__main__":
    aku = Lehti("Aku Ankka", "Aki Hyyppä")
    hytti = Kirja("Hytti nro 6", "Rosa Liksom", 200)

    aku.tulosta_tiedot()
    hytti.tulosta_tiedot()