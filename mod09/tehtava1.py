class Auto:

  def __init__(self, rekisteritunnus, huippunopeus):
    self.rekisteritunnus = rekisteritunnus
    self.huippunopeus = huippunopeus
    self.tammanhetkinen_nopeus = 0
    self.kuljettu_matka = 0


# Pääohjelma
uusi_auto = Auto("ABC-123", 142)

print(f"Rekisteritunnus: {uusi_auto.rekisteritunnus}")
print(f"Huippunopeus: {uusi_auto.huippunopeus} km/h")
print(f"Tämänhetkinen nopeus: {uusi_auto.tammanhetkinen_nopeus} km/h")
print(f"Kuljettu matka: {uusi_auto.kuljettu_matka} km")