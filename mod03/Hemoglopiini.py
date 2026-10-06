sukupuoli = input("Anna biologinen sukupuolesi (M/N): ").upper()

if sukupuoli in ["M", "N"]:
    hemoglobiini = int(input("Anna hemoglobiiniarvosi (g/l): "))
    
    # Miehet (viitearvo 134–195 g/l)
    if sukupuoli == "M":
        if hemoglobiini < 134:
            print("Hemoglobiiniarvo on alhainen.")
        elif hemoglobiini > 195:
            print("Hemoglobiiniarvo on korkea.")
        else:
            print("Hemoglobiiniarvo on normaali.")

    # Naiset (viitearvo 117–175 g/l)
    elif sukupuoli == "N":
        if hemoglobiini < 117:
            print("Hemoglobiiniarvo on alhainen.")
        elif hemoglobiini > 175:
            print("Hemoglobiiniarvo on korkea.")
        else:
            print("Hemoglobiiniarvo on normaali.")
else:
    print("Virheellinen syöte! Anna sukupuoleksi M tai N.")