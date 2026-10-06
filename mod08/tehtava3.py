lentoasemat = {}

while True:
    print("\nValitse toiminto:")
    print("1 = Syötä uusi lentoasema")
    print("2 = Hae lentoaseman tiedot")
    print("3 = Lopeta")
    valinta = input("Valintasi (1-3): ")

    if valinta == "1":
        icao = input("Anna ICAO-koodi: ").upper()
        nimi = input("Anna lentoaseman nimi: ")
        lentoasemat[icao] = nimi
        print(f"Lentoasema {nimi} ({icao}) tallennettu.")
    elif valinta == "2":
        icao = input("Anna haettavan lentoaseman ICAO-koodi: ").upper()
        if icao in lentoasemat:
            print(f"Lentoasema: {lentoasemat[icao]}")
        else:
            print("Lentoasemaa ei löytynyt.")
    elif valinta == "3":
        print("Ohjelma lopetettu.")
        break
    else:
        print("Virheellinen valinta, yritä uudelleen.")
        