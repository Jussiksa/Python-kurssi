from typing import Optional
from peliprojekti.esine import Esine


class Huone:
    def __init__(self, nimi: str, esine: Optional[Esine] = None):
        self.nimi = nimi
        self.esine = esine

    def __str__(self):
        return self.nimi
    