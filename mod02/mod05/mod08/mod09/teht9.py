k1_rotu = 'Mastiffi'
k1_nimi = 'Wuffe'
k1_syntymävuosi = 2022

k2_rotu = 'Bokseri'
k2_nimi = 'Lissu'
k2_syntymävuosi = 2025

k3_rotu = 'Labradori'
k3_nimi = 'Sisu'
k3_syntymävuosi = 2020

'''
class Koira:
        pass

# Luokka on kuin suunnitelma. Olio on sen perusteella rakennettu yksilö

koira = Koira()
koira2 = Koira()

koira.nimi = "Wuffe"
koira.rotu = "Mastiffi"

koira2.nimi = "Lissu"
koira2.rotu = "Bokseri"

print('Ensimmäisen koiran nimi:', koira.nimi)
print('Ensimmäisen koiran rotu:', koira.rotu)

print('Toisen koiran nimi:', koira2.nimi)
print('TOoisen koiran rotu:', koira2.rotu)

'''

# teimme juuri luokan Koira ilman ominaisuuksia
# tämän jälkeen määrittelimme ominaisuudet yksi kerrallaa == työlästä!!!!

# Näin teemme oikeasti:
# Oliossa määritellään ns. tieto ja toiminta

# Koira:

# Koiran ominaisuudet
# - nimi
# - rotu
# - syntymävuosi

# Koiran toiminnot
# - Hauku
# - Syö
# - Nuku


class Koira:

    # Luokkamuuttuja
    tehty = 0
    
    def __init__(self, nimi, rotu, syntymävuosi, haukahdus='Viuviu'):
        self.nimi = nimi
        self.rotu = rotu
        self.syntymävuosi = syntymävuosi
        self.haukahdus = haukahdus
        self.luokitus = 'nisäkäs'
        Koira.tehty += 1

    def hauku(self, kerrat):
        print(f'{self.nimi} tervehtii sinua')
        for i in range(kerrat):
            print(self.haukahdus)


koira = Koira("Lissu", "Bokseri", 2022, "Hau Hau")
koira2 = Koira("Wuffe", "Mastiffi", 2025, "Woof Woof")
koira3 = Koira("Fifi", "Puudeli", 2015)

print(f"Koiria on nyt {Koira.tehty}.")

koira.hauku(2)
print()
koira2.hauku(3)
print()
koira3.hauku(1)


print(f'1. koiran nimi on {koira.nimi} ja rotu {koira.rotu}, vuosi {koira.syntymävuosi}')
print(f'2. koiran nimi on {koira2.nimi} ja rotu {koira2.rotu}')

# print(koira) - viittaus olioon, ei muuttuja


# players = [
#     {
#         "name": "Player 1",
#         "skill_level": 10,
#         "inventory": {"map", "knife"}
#     },
#     {
#         "name": "c",
#         "skill_level": 20,
#         "inventory": {"axe"}
#     }
# ]


# for player in players:
#     print(f"Pelaajan {player['name']} taitotaso on {player['skill_level']}, hallussa:")
#     for item in player["inventory"]:
#         print(f"- {item}")


print()
print('----------')

info = 'Pelaajan tiedot'

class Player:
    def __init__(self, name, skill_level, inventory):

        # ominaisuus = parametrina tullut arvo
        self.name = name
        self.skill_level = skill_level
        self.inventory = inventory

    def show_info(self):
        print(info)
        print('Pelaajan nimi:', self.name)
        print('Taso:', self.skill_level)
        print('Inventaario:')
        for item in self.inventory:
            print('>',item)
        print('------')

    def add_item(self, item):
        self.inventory.add(item)


player1 = Player('Jussi', 10, {"map", "knife","hammer"})
player2 = Player('Keijo', 20, {"axe"} )

player1.show_info()
# player2.show_info()

player1.add_item("key")
player1.show_info()




# pelaajan tiedot
# print(f'Pelaajan 1 nimi on {player1.name} ja taso on {player1.skill_level}')



### Miten tämä edellinen voitaisiin kuvata luokkana
### Esim. PELAAJA