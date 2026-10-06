# Määritellään vuodenajat monikkona (kuukaudet 1-12)
# Järjestys: 12, 1, 2 = Talvi, 3, 4, 5 = Kevät, 6, 7, 8 = Kesä, 9, 10, 11 = Syksy
vuodenajat = ("Talvi", "Talvi", "Kevät", "Kevät", "Kevät", "Kesä", "Kesä", "Kesä", "Syksy", "Syksy", "Syksy", "Talvi")

kk = int(input("Anna kuukauden numero (1-12): "))

if 1 <= kk <= 12:
    vuodenaika = vuodenajat[kk - 1]
    print(f"{kk}. kuukausi kuuluu vuodenaikaan: {vuodenaika}")
else:
    print("Virheellinen kuukauden numero!")