class Esine:
    def __init__(self, nimi: str, paino: float):
        self.nimi = nimi
        self.paino = paino

    def __str__(self):
        return f"{self.nimi} ({self.paino} kg)"
    