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
        if kohdekerros > self.ylin or kohdekerros < self.alin:
            print("Virheellinen kerros!")
            return

        while self.nykyinen_kerros < kohdekerros:
            self.kerros_ylos()

        while self.nykyinen_kerros > kohdekerros:
            self.kerros_alas()

# Testataan hissiä
if __name__ == "__main__":
    h = Hissi(1, 10)
    print("Siirrytään kerrokseen 5:")
    h.siirry_kerrokseen(5)
    print("\nPalataan alimpaan kerrokseen:")
    h.siirry_kerrokseen(1)
    