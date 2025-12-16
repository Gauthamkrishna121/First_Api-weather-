from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "0d8dc349c55730be10d5583ad7365c72"

@app.route("/", methods=["GET", "POST"])
def home():
    weather_data = None
    error = None

    if request.method == "POST":
        city = request.form.get("city")

        url = "https://api.openweathermap.org/data/2.5/weather"
        params = {
            "q": city,
            "appid": API_KEY,
            "units": "metric"
        }

        response = requests.get(url, params=params)

        if response.status_code == 200:
            weather_data = response.json()
        else:
            error = "City not found! Try another one."

    return render_template("index.html", weather=weather_data, error=error)

if __name__ == "__main__":
    app.run(debug=True)
