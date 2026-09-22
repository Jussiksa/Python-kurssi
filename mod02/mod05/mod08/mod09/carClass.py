 class Auto:

    def __int__(self, rekisteritunnus, huioounopeus).
      self.rekisteritunnus = rekisteritunnus
      self.huippunopeus = huippunopeus = huioounopeus
      self.tamanhetkinen_nopeus = 0
      self.kuljettumatka = 0
      #pääohjelma
      if_-name__ == "__main__":
      #luodaan uusiauto anneteuilla tiedoilla
      uusi_auto = Auto("ABC-123",142)
      #Tulostetaan autonkaikki ominaisuudet
        print("Rekisteritunnus:", uusi_auto.rekisteritunnus:{uusi_auto.rekisteritunnus}")
        print(f"huippunopeus::{uusis_auto huippunopeus} km/h")
        print(f"tämänhetkinen nopeus: {uusiauto_.tamanhetkinen_nopeus} km/h")
        print(f"kuljettu matka:{uusi_auto.kuljettu_matka}km")
    class Auto:

  def __init__(self, rekisteritunnus, huippunopeus):
    self.rekisteritunnus = rekisteritunnus
    self.huippunopeus = huippunopeus
    self.tamanhetkinen_nopeus = 0
    self.kuljettu_matka = 0

  def kiihdytä(self, muutos):
    uusi_nopeus = self.tamanhetkinen_nopeus + muutos
    
    # Tarkistetaan, että nopeus ei ylitä huippunopeutta eikä alita nollaa
    if uusi_nopeus > self.huippunopeus:
      self.tamanhetkinen_nopeus = self.huippunopeus
    elif uusi_nopeus < 0:
      self.tamanhetkinen_nopeus = 0
    else:
      self.tamanhetkinen_nopeus = uusi_nopeus


# Pääohjelma
if __name__ == "__main__":
  # Luodaan uusi auto (rekisteritunnus ABC-123, huippunopeus 142 km/h)
  uusi_auto = Auto("ABC-123", 142)

  # Nostetaan nopeutta annetuilla arvoilla
  uusi_auto.kiihdytä(30)
  uusi_auto.kiihdytä(70)
  uusi_auto.kiihdytä(50)

  # Tulostetaan nopeus kiihdytysten jälkeen (tarkastutaan huippunopeuden rajoitus)
  print(f"Tämänhetkinen nopeus: {uusi_auto.tamanhetkinen_nopeus} km/h")

  # Suoritetaan hätäjarrutus
  uusi_auto.kiihdytä(-200)

  # Tulostetaan uusi nopeus hätäjarrutuksen jälkeen
  print(f"Nopeus hätäjarrutuksen jälkeen: {uusi_auto.tamanhetkinen_nopeus} km/h")        
      _
