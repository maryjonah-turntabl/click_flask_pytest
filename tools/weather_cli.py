import click
import requests


def get_json__weather_details(city_name):

    base_url = "https://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "appid=" + "de04128264d84333b53a1d2455438b31" + "&q=" + city_name

    with click.progressbar(complete_url) as bar:
        response = requests.get(complete_url)
        weather_json = response.json()

    return weather_json


def return_needed_weather_details(weather_details):
    if weather_details["cod"] != "404":
        main_details = weather_details["main"]
        country_name = weather_details["sys"]["country"]
        temperature  = main_details["temp"]
        pressure = main_details["pressure"]
        humidity = main_details["humidity"]

        click.echo(f"It is currently {humidity}% humid".strip())
    else:
        click.echo("OpenWeather does not have information for this location.")


@click.command()
def weather():
    """ Provides user city name"""

    city = click.prompt("City Name")
    city = city.strip()
    weather_details = get_json__weather_details(city)
    return_needed_weather_details(weather_details)


# 1 - create a fxn to compose endpoint and call fxn
# 2 - create another fxn to get the required details needed
# 3 - then in weather, after prompting the user, call fxn 1 and then call 2 to display the details

