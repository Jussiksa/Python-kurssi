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


# Pääohjelma
uusi_auto = Auto("ABC-123", 142)

# Asetetaan nopeudeksi 60 km/h ja kuljetaan aluksi vähän
uusi_auto.kiihdyta(60)
uusi_auto.kulje(1.5)  # 1.5 tuntia -> 90 km
print(f"Kuljettu matka ensimmäisen ajon jälkeen: {uusi_auto.kuljettu_matka} km")
