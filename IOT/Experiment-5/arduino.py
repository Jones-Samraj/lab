import requests
import time
import random

server_url = "http://127.0.0.1:5000/data"

while True:
    temperature = random.randint(20, 30)
    humidity = random.randint(40, 70)

    data = {
        'temperature': temperature,
        'humidity': humidity
    }

    try:
        response = requests.post(server_url, data=data)
        print(
            f"Temperature: {temperature}°C, "
            f"Humidity: {humidity}%, "
            f"Response: {response.text}"
        )
    except Exception as e:
        print("Error:", e)

    time.sleep(5)