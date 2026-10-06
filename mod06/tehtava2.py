import random


def heita_noppaa(tahkot):
  return random.randint(1, tahkot)


if __name__ == "__main__":
  maksimi = int(input("Anna nopan tahkojen määrä: "))
  tulos = 0
  while tulos != maksimi:
    tulos = heita_noppaa(maksimi)
    print(f"Heitto: {tulos}")