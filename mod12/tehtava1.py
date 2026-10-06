import requests

def hae_vitsi():
    pyynto = "https://api.chucknorris.io/jokes/random"
    
    try:
        vastaus = requests.get(pyynto)
        if vastaus.status_code == 200:
            json_data = vastaus.json()
            print(json_data["value"])
        else:
            print("Pyyntö epäonnistui statuskoodilla:", vastaus.status_code)
    except requests.exceptions.RequestException as e:
        print("Verkkovirhe:", e)

if __name__ == "__main__":
    hae_vitsi()