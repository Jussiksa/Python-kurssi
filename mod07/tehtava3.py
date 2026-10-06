def gallonat_litroiksi(gallonat):
  return gallonat * 3.785


if __name__ == "__main__":
  while True:
    maara = float(
        input("Anna bensiinin määrä Yhdysvaltain gallonaina (negatiivinen"
              " lopettaa): ")
    )
    if maara < 0:
      print("Ohjelma päättyi.")
      break
    litrat = gallonat_litroiksi(maara)
    print(f"{maara} gallonaa on {litrat:.3f} litraa.")