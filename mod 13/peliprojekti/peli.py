import random
import time


class SimoKusetusPeli:
  """SimoKusetusPeli - Tekstipohjainen seikkailupeli, jossa yritetään kusettaa/ulkoiluttaa Simo-koiraa turvallisesti puun luo."""

  def __init__(self):
    self.koiran_sijainti = 0
    self.puun_sijainti = 8
    self.koti_sijainti = 0

    self.hihnan_kunto = 5
    self.hihnan_maksimi = 5
    self.simon_kiukku = 0
    self.kakkapussit = 3
    self.herkut = 2
    self.pissat_tehty = False
    self.kakkat_tehty = False
    self.vuorot = 0

    self.saatilat = ["Aurinkoinen", "Sateinen", "Luminen", "Tuulinen"]
    self.nykyinen_saa = random.choice(self.saatilat)

  def nayta_intro(self):
    try:
      with open("intro.txt", "r", encoding="utf-8") as f:
        print(f.read())
    except FileNotFoundError:
      print("=== SIMON KUSETUSPELI ===")
    print(f"Päivän sää ulkona: {self.nykyinen_saa}\n")

  def piirra_kartta(self):
    polku = ["_"] * (self.puun_sijainti + 2)
    polku[self.puun_sijainti] = "🌳"
    polku[self.koti_sijainti] = "🏠"

    if self.koiran_sijainti == self.puun_sijainti:
      polku[self.koiran_sijainti] = "🐕🌳"
    else:
      polku[self.koiran_sijainti] = "🐕"

    print("\nPOLKU: " + " - ".join(polku))

  def nayta_tilanne(self):
    print(f"\n--- Tilannekatsaus (Vuoro {self.vuorot}) ---")
    print(f"Koiran sijainti polulla: {self.koiran_sijainti}")
    print(f"Puun sijainti: {self.puun_sijainti}")
    print(
        f"Hihnan kunto: {self.hihnan_kunto}/{self.hihnan_maksimi}"
        f" {'⚠️' if self.hihnan_kunto <= 2 else '✅'}"
    )
    print(f"Simon kiukutustaso: {self.simon_kiukku}/10")
    print(
        f"Repussa: Herkkuja: {self.herkut} | Kakkapusseja: {self.kakkapussit}"
    )
    self.piirra_kartta()

  def satunnaistapahtuma(self):
    nopanheitto = random.randint(1, 10)
    if nopanheitto == 1:
      print("\n🐿️  Simo näkee oravan! Se kiskaisee raivokkaasti eteenpäin!")
      self.hihnan_kunto -= 1
      self.simon_kiukku += 2
      self.koiran_sijainti = min(
          self.puun_sijainti + 1, self.koiran_sijainti + 1
      )
    elif nopanheitto == 2:
      print(
          "\n🦴  Simo löytää vanhan luun maasta ja alkaa jyrsiä sitä"
          " tyytyväisenä."
      )
      self.simon_kiukku = max(0, self.simon_kiukku - 2)
    elif nopanheitto == 3:
      print("\n🚗  Auto ajaa ohi ja roiskauttaa vettä! Simo säikähtää.")
      self.simon_kiukku += 1
    elif nopanheitto == 4 and not self.kakkat_tehty:
      print("\n💩  Simo pysähtyy ja tekee tarpeensa kesken matkan!")
      self.kakkat_tehty = True
      if self.kakkapussit > 0:
        print("Korjaat kakat talteen pussiin. Hienoa toimintaa!")
        self.kakkapussit -= 1
      else:
        print(
            "Sinulla ei ole kakkapusseja! Naapurit katsovat paheksuvasti (+2"
            " kiukku)."
        )
        self.simon_kiukku += 2

  def anna_herkku(self):
    if self.herkut > 0:
      self.herkut -= 1
      self.simon_kiukku = max(0, self.simon_kiukku - 3)
      print("\n🍖 Annoit Simolle maistuvan makupalan! Simo rauhoittuu.")
    else:
      print("\n❌ Taskusi ovat tyhjät! Ei herkkuja jäljellä.")

  def korjaa_hihnaa(self):
    if self.hihnan_kunto < self.hihnan_maksimi:
      print("\n🧵 Solmit ja teippaat hihnan kuluneita kohtia.")
      self.hihnan_kunto = min(self.hihnan_maksimi, self.hihnan_kunto + 2)
      print(f"Hihnan kunto on nyt {self.hihnan_kunto}.")
    else:
      print("\n✅ Hihna on jo täydellisessä kunnossa!")

  def siirry_eteenpain(self):
    print("\n🚶 Houkuttelet Simoa astumaan askeleen eteenpäin...")
    self.koiran_sijainti += 1

    puremisriski = random.randint(1, 10) + self.simon_kiukku
    if puremisriski > 7:
      print("💥 Simo saa yhtäkkisen hepulin ja purees hihnaa!")
      self.hihnan_kunto -= 1
    else:
      print("Simo kävelee kiltisti mukana.")

    self.satunnaistapahtuma()

  def siirry_taaksepain(self):
    if self.koiran_sijainti > 0:
      print("\n⬅️ Peruutat hieman ja kutsut Simoa lähellesi...")
      self.koiran_sijainti -= 1
      self.simon_kiukku = max(0, self.simon_kiukku - 1)
    else:
      print("\nOlette jo kotiovella, et voi mennä kauemmas taaksepäin!")

  def pissata_koira(self):
    if self.koiran_sijainti == self.puun_sijainti:
      print("\n🌳 Simo haistelee puun runkoa pitkään ja hartaasti...")
      time.sleep(1)
      print("💦 Yesss! Simo nostaa jalkaansa ja kusetus onnistui!")
      self.pissat_tehty = True
    else:
      print("\n❌ Tästä puuttuu kunnon puu! Simo ei suostu pissaamaan.")
      self.simon_kiukku += 1

  def tarkista_pelin_loppu(self):
    if self.hihnan_kunto <= 0:
      print("\n💥 Hihna katkesi kokonaan! Simo säntää karkuun!")
      print("HÄVISIT PELIN!")
      return True

    if self.simon_kiukku >= 10:
      print("\n🤬 Simo sai raivokohtauksen ja kieltäytyy liikkumasta!")
      print("HÄVISIT PELIN!")
      return True

    if self.pissat_tehty:
      print("\n🎉 ONNITTELUT! Tehtävä suoritettu!")
      print(f"Selvisit lenkistä {self.vuorot} vuorossa!")
      return True

    return False

  def pelaa(self):
    self.nayta_intro()

    while True:
      self.vuorot += 1
      self.nayta_tilanne()

      print("\nMitä teet seuraavaksi?")
      print("1. Houkuttele Simoa askel eteenpäin 🚶")
      print("2. Peruuta askel taaksepäin ⬅️")
      print("3. Anna Simolle herkku 🍖")
      print("4. Korjaa / vahvista hihnaa 🧵")
      print("5. Yritä kusettaa Simoa (Pissata puulle) 💦")
      print("6. Lopeta lenkki ja luovuta 🚪")

      valinta = input("\nValitse toiminto (1-6): ").strip()

      if valinta == "1":
        self.siirry_eteenpain()
      elif valinta == "2":
        self.siirry_taaksepain()
      elif valinta == "3":
        self.anna_herkku()
      elif valinta == "4":
        self.korjaa_hihnaa()
      elif valinta == "5":
        self.pissata_koira()
      elif valinta == "6":
        print("\nLuovutit lenkin ja palasit kotiin. Peli päättyi.")
        break
      else:
        print("\nTuntematon komento!")

      if self.tarkista_pelin_loppu():
        break

      time.sleep(0.5)