pituus = float(input("Anna kuhan pituus senttimetreinä: "))

puuttuva_pituus = 37 - pituus

if pituus < 37:
    print(f"Kuja on alamittainen!\n\nLaske kuha takaisin järveen. Se on {puuttuva_pituus:.1f} cm liian lyhyt.")
else:
    print("Kuha on pyyntimitassa!")