class Hissi:
    def __init__(self, alin_kerros, ylin_kerros, nimi="Hissi"):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.nykyinen_kerros = alin_kerros  # Uusi hissi aloittaa alimmasta kerroksesta
        self.nimi = nimi

    def kerros_ylös(self):
        if self.nykyinen_kerros < self.ylin_kerros:
            self.nykyinen_kerros += 1
            print(f"{self.nimi} on nyt kerroksessa {self.nykyinen_kerros}")

    def kerros_alas(self):
        if self.nykyinen_kerros > self.alin_kerros:
            self.nykyinen_kerros -= 1
            print(f"{self.nimi} on nyt kerroksessa {self.nykyinen_kerros}")

    def siirry_kerrokseen(self, kohdekerros):
        # Tarkistetaan, että kohdekerros on rakennuksen sallituissa rajoissa
        if kohdekerros > self.ylin_kerros:
            kohdekerros = self.ylin_kerros
        elif kohdekerros < self.alin_kerros:
            kohdekerros = self.alin_kerros

        # Siirretään hissiä kerros kerrallaan kohti kohdetta
        while self.nykyinen_kerros < kohdekerros:
            self.kerros_ylös()
        while self.nykyinen_kerros > kohdekerros:
            self.kerros_alas()


class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissien_lukumäärä):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.hissit = []
        
        # Luodaan taloon tarvittava määrä hissejä ja annetaan niille nimikyltit
        for i in range(hissien_lukumäärä):
            hissi_nimi = f"Hissi {i + 1}"
            uusi_hissi = Hissi(alin_kerros, ylin_kerros, hissi_nimi)
            self.hissit.append(uusi_hissi)

    def aja_hissiä(self, hissin_numero, kohdekerros):
        # Tarkistetaan, että annettu hissin numero on olemassa (1-pohjainen indeksointi)
        if 1 <= hissin_numero <= len(self.hissit):
            hissi = self.hissit[hissin_numero - 1]
            print(f"\nAjetaan hissiä {hissin_numero} kerrokseen {kohdekerros}:")
            hissi.siirry_kerrokseen(kohdekerros)
        else:
            print(f"Virhe: Hissiä numero {hissin_numero} ei löydy talosta.")

    def palohälytys(self):
        print("\n🚨 PALOHÄLYTYS! Kaikki hissit ajetaan alimpaan kerrokseen! 🚨")
        for i, hissi in enumerate(self.hissit):
            print(f"\nSiirretään hissi {i + 1} alas:")
            hissi.siirry_kerrokseen(self.alin_kerros)


if __name__ == "__main__":
    print("=== LUODAAN TALO ===")
    # Luodaan talo: kerrokset 2–12, ja talossa on 3 hissiä
    talo = Talo(2, 12, 3)
    print(f"Talo luotu. Kerrokset: {talo.alin_kerros}-{talo.ylin_kerros}, hissejä: {len(talo.hissit)}\n")

    print("=== PÄÄOHJELMA: Ajelemista talon hisseillä ===")
    talo.aja_hissiä(1, 8)
    talo.aja_hissiä(2, 5)
    talo.aja_hissiä(3, 11)

    # Testataan palohälytystä, joka palauttaa kaikki hissit pohjakerrokseen (2)
    talo.palohälytys()