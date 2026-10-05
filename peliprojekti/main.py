from esine import Esine
from huone import Huone
from pelaaja import Pelaaja

def alusta_peli():
    # Luo esineet
    avain = Esine("Aarreavain", 0.2)
    miekka = Esine("Ruosteinen miekka", 3.5)

    # Luo huoneet ja aseta esineet
    eteinen = Huone("Eteinen", avain)
    kirjasto = Huone("Kirjasto", miekka)
    puutarha = Huone("Puutarha", None)

    # Luo pelaaja aloitushuoneeseen
    pelaaja_nimi = input("Syötä hahmosi nimi: ").strip() or "Seikkailija"
    pelaaja = Pelaaja(pelaaja_nimi, eteinen)

    # Sanakirja liikkumista varten
    huoneet = {
        "1": eteinen,
        "2": kirjasto,
        "3": puutarha
    }

    return pelaaja, huoneet


def main():
    pelaaja, huoneet = alusta_peli()

    while True:
        pelaaja.nayta_tiedot()
        print("\n--- VALIKKO ---")
        print("1. Liiku toiseen huoneeseen")
        print("2. Kerää esine huoneesta")
        print("3. Lopeta peli")

        valinta = input("Valitse toiminto (1-3): ").strip()

        if valinta == "1":
            print("\nMihin huoneeseen haluat siirtyä?")
            for avain, huone in huoneet.items():
                print(f"{avain}. {huone.nimi}")
            
            kohde_valinta = input("Valitse huone: ").strip()
            if kohde_valinta in huoneet:
                pelaaja.liiku(huoneet[kohde_valinta])
            else:
                print("\nTuntematon huone.")

        elif valinta == "2":
            pelaaja.keraa_esine()

        elif valinta == "3":
            print("\nKiitos pelaamisesta!")
            break
        else:
            print("\nVirheellinen valinta, yritä uudelleen.")


if __name__ == "__main__":
    main()
    import os
import json

# Tiedostopolut
INTRO_FILE = "intro.txt"
OHJEET_FILE = "ohjeet.txt"
SAVE_FILE = "tallennus.json"


def lue_tiedosto(tiedostopolku):
    """Lukee tekstitiedoston sisällön ja palauttaa sen merkkijonona."""
    if os.path.exists(tiedostopolku):
        with open(tiedostopolku, "r", encoding="utf-8") as f:
            return f.read()
    else:
        return f"[Tiedostoa {tiedostopolku} ei löytynyt.]"


def näytä_intro_ja_ohjeet():
    """Lukee ja tulostaa intromateriaalin sekä ohjeet."""
    print(lue_tiedosto(INTRO_FILE))
    print(lue_tiedosto(OHJEET_FILE))


def lataa_kaikki_tallennukset():
    """Lataa kaikkien pelaajien tallennukset JSON-tiedostosta."""
    if os.path.exists(SAVE_FILE):
        try:
            with open(SAVE_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return {}
    return {}


def tallenna_peli(pelaajan_nimi, pelitilanne):
    """Tallenna tietyn pelaajan tilanne tiedostoon."""
    tallennukset = lataa_kaikki_tallennukset()
    tallennukset[pelaajan_nimi.lower()] = pelitilanne
    
    with open(SAVE_FILE, "w", encoding="utf-8") as f:
        json.dump(tallennukset, f, ensure_ascii=False, indent=4)
    print("\nPeli tallennettu onnistuneesti!")


def lataa_peli(pelaajan_nimi):
    """Lataa pelaajan tilanteen nimen perusteella."""
    tallennukset = lataa_kaikki_tallennukset()
    return tallennukset.get(pelaajan_nimi.lower(), None)


def pääpeli():
    # 1. Lue ja tulosta esittely ja ohjeet
    näytä_intro_ja_ohjeet()

    # 2. Kysy pelaajan nimi jatkamista tai uutta peliä varten
    pelaajan_nimi = input("Anna pelaajanimesi: ").strip()
    if not pelaajan_nimi:
        pelaajan_nimi = "Pelaaja1"

    tallennettu_tilanne = lataa_peli(pelaajan_nimi)

    if tallennettu_tilanne:
        print(f"\nTervetuloa takaisin, {pelaajan_nimi}!")
        valinta = input("Löydettiin tallennettu peli. Haluatko jatkaa? (k/e): ").strip().lower()
        if valinta == 'k':
            pelitilanne = tallennettu_tilanne
            print(f"Jatketaan tasolta {pelitilanne['taso']} (Pisteet: {pelitilanne['pisteet']}).")
        else:
            pelitilanne = {"taso": 1, "pisteet": 0, "nimi": pelaajan_nimi}
            print("Aloitetaan uusi peli.")
    else:
        print(f"\nTervetuloa uusi pelaaja {pelaajan_nimi}!")
        pelitilanne = {"taso": 1, "pisteet": 0, "nimi": pelaajan_nimi}

    # 3. Pelisilmukka
    while True:
        print(f"\n--- TILANNE: Taso {pelitilanne['taso']} | Pisteet {pelitilanne['pisteet']} ---")
        komento = input("Mitä teet? (pelaa / tallenna / lopeta): ").strip().lower()

        if komento == "pelaa":
            pelitilanne["pisteet"] += 10
            pelitilanne["taso"] += 1
            print(f"Pelasit kierroksen! Taso nousi ja sait 10 pistettä.")
        elif komento == "tallenna":
            tallenna_peli(pelaajan_nimi, pelitilanne)
        elif komento == "lopeta":
            varmistus = input("Haluatko tallentaa ennen lopetusta? (k/e): ").strip().lower()
            if varmistus == 'k':
                tallenna_peli(pelaajan_nimi, pelitilanne)
            print("Kiitos pelaamisesta! Nähdään taas.")
            break
        else:
            print("Tuntematon komento. Kokeile: pelaa, tallenna tai lopeta.")


if __name__ == "__main__":
    pääpeli()