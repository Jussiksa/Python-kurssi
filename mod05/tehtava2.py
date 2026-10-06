while True:
  tuumat = float(
      input("Anna tuumat (negatiivinen luku lopettaa ohjelman): ")
  )
  if tuumat < 0:
    print("Ohjelma lopetettu.")
    break
  cm = tuumat * 2.54
  print(f"{tuumat} tuumaa = {cm:.2f} cm")