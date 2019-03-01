import random
import time
import requests

# server_url = "http://localhost:80/data"
server_url = "https://air-pollution-rait-2019.herokuapp.com/data"

for i in range(290,1000):
    try:
        co2 = i
        so2 = i
        no2 = i
        print("Sending Data ", co2, so2, no2)
        params = {
            'CO2': co2,
            'SO2': so2,
            'NO2': no2,
        }
        r = requests.get(url=server_url, params=params)
        time.sleep(2)
    except:
        pass
