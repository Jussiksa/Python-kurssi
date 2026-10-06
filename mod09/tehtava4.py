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


# Luodaan 10 autoa listaan
autot = []
for i in range(1, 11):
  rekisteri = f"ABC-{i}"
  huippunopeus = random.randint(100, 200)
  autot.append(Auto(rekisteri, huippunopeus))

kilpailu_kaynnissa = True

# Simuloidaan tunti kerrallaan
while kilpailu_kaynnissa:
  for auto in autot:
    nopeuden_muutos = random.randint(-10, 15)
    auto.kiihdyta(nopeuden_muutos)
    auto.kulje(1)

    if auto.kuljettu_matka >= 10000:
      kilpailu_kaynnissa = False

# Tulostetaan tulokset taulukkona
print(
    f"{'Rekkari':<10} | {'Huippunopeus':<12} | {'Nopeus':<8} |"
    f" {'Matka (km)':<10}"
)
print("-" * 50)
for auto in autot:
  print(
      f"{auto.rekisteritunnus:<10} | {auto.huippunopeus:<10} km/h |"
      f" {auto.tammanhetkinen_nopeus:<6} km/h | {auto.kuljettu_matka:<10.1f} km"
  )