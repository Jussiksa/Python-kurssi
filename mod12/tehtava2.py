import requests

def hae_saa(paikkakunta, api_avain):
    pyynto = f"https://api.openweathermap.org/data/2.5/weather?q={paikkakunta}&appid={api_avain}&units=metric&lang=fi"
    
    try:
        vastaus = requests.get(pyynto)
        if vastaus.status_code == 200:
            data = vastaus.json()
            saa_kuvaus = data["weather"][0]["description"]
            lampotila = data["main"]["temp"]
            
            print(f"\nSää paikkakunnalla {paikkakunta.capitalize()}:")
            print(f"Kuvaus: {saa_kuvaus.capitalize()}")
            print(f"Lämpötila: {lampotila:.1f} °C")
        elif vastaus.status_code == 404:
            print("Paikkakuntaa ei löytynyt. Tarkista kirjoitusasu.")
        else:
            print("Virhe haettaessa säätietoja. Statuskoodi:", vastaus.status_code)
    except requests.exceptions.RequestException as e:
        print("Verkkovirhe:", e)

if __name__ == "__main__":
    paikkakunta = input("Syötä paikkakunnan nimi: ")
    # Korvaa alla oleva merkkijono omalla OpenWeather API -avaimellasi:
    API_KEY = "OMARAPAJINPA_API_KEY" 
    
    hae_saa(paikkakunta, API_KEY)