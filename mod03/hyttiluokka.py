Tässä laivan hyttiluokkatehtävän (cabin.py) käännös suomeksi ja samaan tapaan siistitty, napakka versio:

Python
hytti = input("Anna hyttiluokka (LUX, A, B, C): ").upper()

if hytti == "LUX":
    print("LUX on parvekkeellinen hytti ylädekellä.")
elif hytti == "A":
    print("A on ikkunallinen hytti autokannen yläpuolella.")
elif hytti == "B":
    print("B on ikkunaton hytti autokannen yläpuolella.")
elif hytti == "C":
    print("C on ikkunaton hytti autokannen alapuolella.")
else:
    print("Virheellinen hyttiluokka!")