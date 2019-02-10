import random
import time
import requests

server_url = "http://localhost:5000/data"

while True:
    try:
        co2 = random.randint(0, 100)
        so2 = random.randint(0, 100)
        no2 = random.randint(0, 100)
        print("Sending Data ", co2, so2, no2)
        params = {
            'CO2': co2,
            'SO2': so2,
            'NO2': no2,
        }
        r = requests.get(url=server_url, params=params)
        time.sleep(0.5)
    except:
        pass
