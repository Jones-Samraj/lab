from flask import Flask, request

app = Flask(__name__)

@app.route('/data', methods=['POST'])
def receive_data():
    temperature = request.form.get('temperature')
    humidity = request.form.get('humidity')

    print(f"Temperature: {temperature}°C, Humidity: {humidity}%")
    return "Data received", 200

app.run(host="0.0.0.0", port=5000)