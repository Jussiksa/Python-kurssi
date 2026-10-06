import random

# Kolmenumeroinen koodi (0-9)
koodi_3 = f"{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}"

# Nelinumeroinen koodi (1-6)
koodi_4 = f"{random.randint(1, 6)}{random.randint(1, 6)}{random.randint(1, 6)}{random.randint(1, 6)}"

print(f"3-numeroinen koodi (0-9): {koodi_3}")
print(f"4-numeroinen koodi (1-6): {koodi_4}")