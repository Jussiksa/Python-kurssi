class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tammanhetkinen_nopeus = 0
        self.kuljettu_matka = 0

    def kiihdyta(self, nopeuden_muutos):
        uusi_nopeus = self.tammanhetkinen_nopeus + nopeuden_muutos
        if uusi_nopeus > self.huippunopeus:
            self.tammanhetkinen_nopeus = self.huippunopeus
        elif uusi_nopeus < 0:
            self.tammanhetkinen_nopeus = 0
        else:
            self.tammanhetkinen_nopeus = uusi_nopeus

    def kulje(self, tunnit):
        self.kuljettu_matka += self.tammanhetkinen_nopeus * tunnit


class Sahkoauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti):
        super().__init__(rekisteritunnus, huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti


class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, tankin_koko):
        super().__init__(rekisteritunnus, huippunopeus)
        self.tankin_koko = tankin_koko


# Pääohjelma
if __name__ == "__main__":
    sahkoauto = Sahkoauto("ABC-15", 180, 52.5)
    polttomoottori = Polttomoottoriauto("ACD-123", 165, 32.3)

    # Asetetaan nopeudet
    sahkoauto.kiihdyta(120)
    polttomoottori.kiihdyta(150)

    # Ajetaan 3 tuntia
    sahkoauto.kulje(3)
    polttomoottori.kulje(3)

    # Tulostetaan matkamittarilukemat
    print(f"Sähköauton ({sahkoauto.rekisteritunnus}) mittarilukema: {sahkoauto.kuljettu_matka} km")
    print(f"Polttomoottoriauton ({polttomoottori.rekisteritunnus}) mittarilukema: {polttomoottori.kuljettu_matka} km")