luku1 = int(input("Anna ensimmäinen luku: "))
luku2 = int(input("Anna toinen luku: "))
luku3 = int(input("Anna kolmas luku: "))

luvut = [luku1, luku2, luku3]

summa = sum(luvut)
tulo = luku1 * luku2 * luku3
keskiarvo = summa / len(luvut)

print(f"Lukujen summa: {summa}")
print(f"Lukujen tulo: {tulo}")
print(f"Lukujen keskiarvo: {keskiarvo:.2f}")