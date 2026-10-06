class Hissi:
    def __init__(self, alin_kerros, ylimmat_kerros):
        self.alin = alin_kerros
        self.ylin = ylimmat_kerros
        self.nykyinen_kerros = alin_kerros

    def kerros_ylos(self):
        if self.nykyinen_kerros < self.ylin:
            self.nykyinen_kerros += 1
            print(f"Hissi on kerroksessa {self.nykyinen_kerros}")

    def kerros_alas(self):
        if self.nykyinen_kerros > self.alin:
            self.nykyinen_kerros -= 1
            print(f"Hissi on kerroksessa {self.nykyinen_kerros}")

    def siirry_kerrokseen(self, kohdekerros):
        while self.nykyinen_kerros < kohdekerros:
            self.kerros_ylos()
        while self.nykyinen_kerros > kohdekerros:
            self.kerros_alas()


class Talo:
    def __init__(self, alin_kerros, ylimmat_kerros, hissien_lkm):
        self.alin = alin_kerros
        self.ylin = ylimmat_kerros
        self.hissit = [Hissi(alin_kerros, ylimmat_kerros) for _ in range(hissien_lkm)]

    def aja_hissia(self, hissin_numero, kohdekerros):
        if 0 <= hissin_numero < len(self.hissit):
            print(f"\nAjetaan hissiä numero {hissin_numero + 1} kerrokseen {kohdekerros}:")
            self.hissit[hissin_numero].siirry_kerrokseen(kohdekerros)

    def palohalytys(self):
        print("\n!!! PALOHÄLYTYS !!! KAIKKI HISSIT POHJAKERROKSEEN!")
        for i, hissi in enumerate(self.hissit):
            print(f"\nSiirretään hissi {i + 1} pohjakerrokseen:")
            hissi.siirry_kerrokseen(self.alin)


# Testataan palohälytystä
if __name__ == "__main__":
    talo = Talo(1, 10, 3)
    talo.aja_hissia(0, 8)
    talo.aja_hissia(1, 5)
    talo.palohalytys()
    