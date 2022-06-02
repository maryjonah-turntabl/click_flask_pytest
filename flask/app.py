import requests
from flask import Flask, render_template, request

app = Flask(__name__)


def get_json__weather_details(city_name):

    base_url = "https://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "appid=" + "bb37c52c09b87c912cb9199610561cde" + "&q=" + city_name

    response = requests.get(complete_url)
    weather_json = response.json()

    return weather_json


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/results', methods=['POST'])
def return_needed_weather_details():
    city_name = request.form['cityName']
    data = get_json__weather_details(city_name)

    if data["cod"] != "404":
        main_details = data["main"]
        country_name = data["sys"]["country"]
        temperature = main_details["temp"]
        pressure = main_details["pressure"]
        humidity = main_details["humidity"]

        return render_template("results.html",
                               city_name=city_name, country_name=country_name, temperature=temperature, pressure=pressure, humidity=humidity)


app.run()
