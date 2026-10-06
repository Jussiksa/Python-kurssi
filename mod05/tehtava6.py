import random

N = int(input("Anna arvottavien pisteiden kokonaismäärä: "))
n = 0
i = 0

while i < N:
  x = random.uniform(-1, 1)
  y = random.uniform(-1, 1)

  # Testataan onko piste yksikköympyrän sisällä (x^2 + y^2 < 1)
  if x**2 + y**2 < 1:
    n += 1
  i += 1

pii_likiarvo = 4 * n / N
print(f"Piin likiarvo syötetyllä pistemäärällä on noin: {pii_likiarvo}")