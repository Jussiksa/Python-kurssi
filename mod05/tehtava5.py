yritykset = 0

while yritykset < 5:
  tunnus = input("Käyttäjätunnus: ")
  salasana = input("Salasana: ")

  if tunnus == "python" and salasana == "rules":
    print("Tervetuloa")
    break
  else:
    yritykset += 1
    if yritykset < 5:
      print("Väärä tunnus tai salasana. Yritä uudelleen.\n")

if yritykset == 5:
  print("Pääsy evätty.")