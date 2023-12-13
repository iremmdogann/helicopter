import requests

# Tüm helikopterleri getir
response_all = requests.get("http://127.0.0.1:5000/helicopters")
print("Tüm Helikopterler:", response_all.json())

# Belirli bir helikopteri getir (örneğin, helikopter_id = 1)
response_single = requests.get("http://127.0.0.1:5000/helicopters/1")
print("Belirli Helikopter:", response_single.json())
