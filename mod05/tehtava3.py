luvut = []

while True:
  syote = input("Anna luku (tyhjä merkkijono lopettaa): ")
  if syote == "":
    break
  luvut.append(float(syote))

if luvut:
  print(f"Pienin luku: {min(luvut)}")
  print(f"Suurin luku: {max(luvut)}")
else:
  print("Lukuja ei syötetty.")