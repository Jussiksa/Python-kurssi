from typing import List
from peli.huone import Huone
from peli.esine import Esine


from typing import Optional
from peli.esine import Esine

class Pelaaja:
    def __init__(self, nimi: str, aloitushuone: Huone):
        self.nimi = nimi
        self.sijainti: Huone = aloitushuone
        self.esineet: List[Esine] = []

    def liiku(self, kohde: Huone) -> None:
        self.sijainti = kohde
        print(f"\nLiikuithan huoneeseen: {kohde.nimi}")

    def keraa_esine(self) -> None:
        if self.sijainti.esine is not None:
            keratty = self.sijainti.esine
            self.esineet.append(keratty)
            self.sijainti.esine = None
            print(f"\nKeräsit esineen: {keratty.nimi} ({keratty.paino} kg)")
        else:
            print("\nHuoneessa ei ole mitään kerättävää.")

    def nayta_tiedot(self) -> None:
        print(f"\nPelaaja: {self.nimi}")
        print(f"Sijainti: {self.sijainti.nimi}")
        
        huoneen_esine = self.sijainti.esine.nimi if self.sijainti.esine else "Ei esineitä"
        print(f"Huoneessa näkyy: {huoneen_esine}")

        if self.esineet:
            reppu_str = ", ".join([str(e) for e in self.esineet])
            print(f"Repun sisältö: {reppu_str}")
        else:
            print("Repun sisältö: Tyhjä")
            