class Koira:
    """Edustaa yksittäistä koiraa, sen attribuutteja sekä käyttäytymismenetelmiä."""
    
    # Luokkamuuttuja luotujen instanssien kokonaismäärän seurantaan
    tehty: int = 0

    def __init__(self, nimi: str, rotu: str, syntymävuosi: int, haukahdus: str = 'Viuviu') -> None:
        self.nimi = nimi
        self.rotu = rotu
        self.syntymävuosi = syntymävuosi
        self.haukahdus = haukahdus
        self.luokitus = 'nisäkäs'
        Koira.tehty += 1

    def hauku(self, kerrat: int) -> None:
        """Suorittaa koiran tervehdystoiminnon määritetyllä toistomäärällä."""
        print(f'{self.nimi} ({self.rotu}) tervehtii:')
        for _ in range(kerrat):
            print(f'  -> {self.haukahdus}')


if __name__ == "__main__":
    # Järjestelmän instansiointi ja testaus
    koirat = [
        Koira("Lissu", "Bokseri", 2022, "Hau Hau"),
        Koira("Wuffe", "Mastiffi", 2025, "Woof Woof"),
        Koira("Fifi", "Puudeli", 2015)
    ]

    print(f"Järjestelmään rekisteröidyt koirat yhteensä: {Koira.tehty}\n")
    print("-" * 40)

    for i, koira in enumerate(koirat, 1):
        koira.hauku(i)
        print(f"Tiedot -> Nimi: {koira.nimi} | Rotu: {koira.rotu} | Syntymävuosi: {koira.syntymävuosi}")
        print("-" * 40)