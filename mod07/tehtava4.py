def laske_summa(luvut):
  return sum(luvut)


if __name__ == "__main__":
  testilista = [3, 7, 12, 5, 20]
  summa = laske_summa(testilista)
  print(f"Listan {testilista} alkioiden summa on: {summa}")
  