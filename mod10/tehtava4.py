import random

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

    def kulje(self, tuntimaara):
        self.kuljettu_matka += self.tammanhetkinen_nopeus * tuntimaara


class Kilpailu:
    def __init__(self, nimi, pituus_km, autot):
        self.nimi = nimi
        self.pituus_km = pituus_km
        self.autot = autot

    def tunti_kuluu(self):
        for auto in self.autot:
            nopeuden_muutos = random.randint(-10, 15)
            auto.kiihdyta(nopeuden_muutos)
            auto.kulje(1)

    def tulostilanne(self):
        print(f"\n--- Kilpailu: {self.nimi} ---")
        print(f"{'Rekkari':<10} | {'Huippunopeus':<12} | {'Nopeus':<8} | {'Matka (km)':<10}")
        print("-" * 55)
        for auto in self.autot:
            print(f"{auto.rekisteritunnus:<10} | {auto.huippunopeus:<10} km/h | {auto.tammanhetkinen_nopeus:<6} km/h | {auto.kuljettu_matka:<10.1f} km")

    def kilpailu_ohi(self):
        for auto in self.autot:
            if auto.kuljettu_matka >= self.pituus_km:
                return True
        return False


# Pääohjelma
if __name__ == "__main__":
    autolista = []
    for i in range(1, 11):
        autolista.append(Auto(f"ABC-{i}", random.randint(100, 200)))

    romuralli = Kilpailu("Suuri romuralli", 8000, autolista)
    tunnit = 0

    while not romuralli.kilpailu_ohi():
        romuralli.tunti_kuluu()
        tunnit += 1
        if tunnit % 10 == 0:
            print(f"\n>>> Kulunut {tunnit} tuntia <<<")
            romuralli.tulostilanne()

    print(f"\n================ KILPAILU PÄÄTTYI! (Kesto: {tunnit}h) ================")
    romuralli.tulostilanne()