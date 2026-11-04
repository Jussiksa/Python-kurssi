from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

def hae_lentokentta_tietokannasta(icao):
    # Yhdistä tietokantaan (päivitä omat tietokantatiedot tarvittaessa)
    yhteys = mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        database="flight_game",
        user="root",
        password=""
    )
    kursori = yhteys.cursor(dictionary=True)
    
    sql = "SELECT ident AS ICAO, name AS Name, municipality AS Municipality FROM airport WHERE ident = %s"
    kursori.execute(sql, (icao.upper(),))
    tulos = kursori.fetchone()
    
    yhteys.close()
    return tulos

@app.route('/kenttä/<icao>', methods=['GET'])
def get_airport(icao):
    kentta = hae_lentokentta_tietokannasta(icao)
    if kentta:
        return jsonify(kentta)
    else:
        return jsonify({"virhe": "Lentokenttää ei löytynyt", "ICAO": icao.upper()}), 404

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=3000)