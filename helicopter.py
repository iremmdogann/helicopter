from flask import Flask, jsonify
import csv

app = Flask(__name__)

# Helikopter veri yapısı (CSV dosyasından yüklenir)
def load_helicopters():
    helicopters = []
    with open('helicopters.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            helicopters.append(row)
    return helicopters

helicopters = load_helicopters()

# Tüm helikopterleri listele
@app.route('/helicopters', methods=['GET'])
def get_helicopters():
    return jsonify(helicopters)

# Belirli bir helikopteri getir
@app.route('/helicopters/<int:helicopter_id>', methods=['GET'])
def get_helicopter(helicopter_id):
    helicopter = next((h for h in helicopters if int(h["id"]) == helicopter_id), None)
    if helicopter:
        return jsonify(helicopter)
    else:
        return jsonify({"message": "Helikopter bulunamadı"}), 404

if __name__ == '__main__':
    # Uygulamayı çalıştır
    app.run(debug=True)
