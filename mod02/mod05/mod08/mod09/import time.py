import time
import random

def play_game():
    print("========================================")
    print("  KIIHDYTYSKISA: HEIDI VS. T-SPORT TOYOTA ")
    print("========================================")
    print("Paina [Enter] vaihtaaksesi vaihdetta ja pitääksesi kierrokset kurissa!")
    print("Valmistaudu... Lähdöstä tulee tiukka.")
    print("-" * 40)
    
    input("Paina Enter aloittaaksesi lähdön!")
    
    heidi_pos = 0.0
    toyota_pos = 0.0
    
    # 5 sekunnin simulaatio
    for second in range(1, 6):
        time.sleep(1)
        
        # Heidi etenee tasaisella ja vahvalla otteella
        heidi_step = random.uniform(15.0, 22.0)
        heidi_pos += heidi_step
        
        # Toyota ampuu korkeilla kierroksilla (VVT-i potkaisee)
        toyota_step = random.uniform(12.0, 25.0)
        toyota_pos += toyota_step
        
        print(f"--- Sekunti {second} ---")
        print(f"Heidi:        {'█' * int(heidi_pos / 5)} ({heidi_pos:.1f} m)")
        print(f"T-Sport Oy:   {'█' * int(toyota_pos / 5)} ({toyota_pos:.1f} m)")
        print("")

    print("=" * 40)
    print("MAALI!")
    
    print(f"Heidin loppumatka: {heidi_pos:.1f} metriä")
    print(f"Toyotan loppumatka: {toyota_pos:.1f} metriä")
    print("-" * 40)
    
    if heidi_pos > toyota_pos:
        print("Voittaja: HEIDI! Räjähtävä lähtö vei voiton!")
    elif toyota_pos > heidi_pos:
        print("Voittaja: T-SPORT TOYOTA! VVT-i huusi punarajalla ohi!")
    else:
        print("Tasan! Kärsäyspeli päättyi täydelliseen tasapeliin.")

if __name__ == "__main__":
    play_game()