import random


class Auto:

  def __init__(self, rekisteritunnus, huippunopeus):
    self.rekisteritunnus = rekisteritunnus
    self.huippunopeus = huippunopeus
    self.tamanhetkinen_nopeus = 0
    self.kuljettu_matka = 0

  def kiihdytä(self, muutos):
    uusi_nopeus = self.tamanhetkinen_nopeus + muutos
    if uusi_nopeus > self.huippunopeus:
      self.tamanhetkinen_nopeus = self.huippunopeus
    elif uusi_nopeus < 0:
      self.tamanhetkinen_nopeus = 0
    else:
      self.tamanhetkinen_nopeus = uusi_nopeus

  def kulje(self, tuntimaara):
    self.kuljettu_matka += self.tamanhetkinen_nopeus * tuntimaara


if __name__ == "__main__":
  print("=== VÄLITESTI 1: Auton luonti ja ominaisuudet ===")
  auto = Auto("ABC-123", 142)
  print(f"Rekisteritunnus: {auto.rekisteritunnus}")
  print(f"Huippunopeus: {auto.huippunopeus} km/h")
  print(f"Tämänhetkinen nopeus: {auto.tamanhetkinen_nopeus} km/h")
  print(f"Kuljettu matka: {auto.kuljettu_matka} km\n")

  print("=== VÄLITESTI 2: Kiihdytys ja hätäjarrutus ===")
  auto.kiihdytä(30)
  auto.kiihdytä(70)
  auto.kiihdytä(50)
  print(f"Nopeus kiihdytysten jälkeen: {auto.tamanhetkinen_nopeus} km/h")
  auto.kiihdytä(-200)
  print(f"Nopeus hätäjarrutuksen jälkeen: {auto.tamanhetkinen_nopeus} km/h\n")

  print("=== VÄLITESTI 3: Matkan kulkeminen ===")
  auto.kiihdytä(60)  # Asetetaan nopeus testiin
  auto.kulje(1.5)  # Ajetaan 1.5 tuntia
  print(f"Kuljettu matka testissä: {auto.kuljettu_matka} km\n")

  print("=== PÄÄOHJELMA: Autokilpailu (10 autoa, maali 10 000 km) ===")
  autot = []
  for i in range(1, 11):
    rekisteritunnus = f"ABC-{i}"
    huippunopeus = random.randint(100, 200)
    autot.append(Auto(rekisteritunnus, huippunopeus))

  kilpailu_kaynnissa = True
  tunnit = 0

  # Kilpailusilmukka
  while kilpailu_kaynnissa:
    tunnit += 1
    for a in autot:
      nopeuden_muutos = random.randint(-10, 15)
      a.kiihdytä(nopeuden_muutos)
      a.kulje(1)

      if a.kuljettu_matka >= 10000:
        kilpailu_kaynnissa = False

  # Tulokset taulukkona
  print(f"\nKilpailu päättyi! Kesto yhteensä: {tunnit} tuntia.\n")
  print(
      f"{'Rekisteritunnus':<15} | {'Huippunopeus (km/h)':<20} |"
      f" {'Tämänhetkinen nopeus (km/h)':<28} | {'Kuljettu matka (km)':<20}"
  )
  print("-" * 93)

  for a in autot:
    print(
        f"{a.rekisteritunnus:<15} | {a.huippunopeus:<20} |"
        f" {a.tamanhetkinen_nopeus:<28} | {a.kuljettu_matka:<20}"
    )