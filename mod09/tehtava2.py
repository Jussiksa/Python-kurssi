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


# Pääohjelma
uusi_auto = Auto("ABC-123", 142)

uusi_auto.kiihdyta(30)
uusi_auto.kiihdyta(70)
uusi_auto.kiihdyta(50)
print(f"Nopeus kiihdytysten jälkeen: {uusi_auto.tammanhetkinen_nopeus} km/h")

uusi_auto.kiihdyta(-200)
print(f"Nopeus hätäjarrutuksen jälkeen: {uusi_auto.tammanhetkinen_nopeus} km/h")