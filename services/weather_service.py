import requests
from models.weather import Weather
from config import API_KEY, BASE_URL

class WeatherService:

    # Esta clase se encarga de comunicarse con la API externa
    # y transformar los datos en objetos Weather
    # No tiene estado, solo métodos

    # Método para obtener el clima de una ciudad
    # Recibe el nombre de la ciudad y devuelve un objeto Weather
    def get_weather(self, city: str) -> Weather:
        params = {
            "q": city,
            "appid": API_KEY,
            "units": "metric",
            "lang": "es"
        }

        # Con try se intenta hacer la petición y manejar errores si ocurren
        try:
            response = requests.get(BASE_URL, params=params)
            response.raise_for_status()  # Lanza un error si la respuesta no es 200
            data = response.json()

            if data.get("cod") != 200:
                raise ValueError(f"Error al obtener el clima: {data.get('message', 'Error desconocido')}")

            return Weather(
                temperature=data["main"]["temp"],
                feels_like=data["main"]["feels_like"],
                humidity=data["main"]["humidity"],
                wind_speed=data["wind"]["speed"],
                description=data["weather"][0]["description"] #weather es una lista y se accede por indice
                )
        
        # Con except se capturan errores específicos
        except requests.exceptions.RequestException as e:
            raise ConnectionError(f"No se pudo conectar con la API: {e}")