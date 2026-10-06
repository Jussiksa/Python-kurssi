from flask import Flask, jsonify

app = Flask(__name__)

def onko_alkuluku(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

@app.route('/alkuluku/<int:luku>', methods=['GET'])
def tarkista_alkuluku(luku):
    tulos = {
        "Number": luku,
        "isPrime": onko_alkuluku(luku)
    }
    return jsonify(tulos)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=3000)