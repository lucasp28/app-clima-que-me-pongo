from services.weather_service import WeatherService
from logic.clothing_advisor import ClothingAdvisor

def main():
    city = input("Ingrese el nombre de la ciudad: ")

    weather_service = WeatherService()
    advisor = ClothingAdvisor()

    try: 
        weather = weather_service.get_weather(city)
        recommendation = advisor.recommend(weather)

        print(f"Clima en: {city}")
        print(f"Descripción: {weather.description}")
        print(f"Temperatura: {weather.temperature}°C, se siente como {weather.feels_like}°C")
        print(f"Humedad: {weather.humidity}%")
        print(f"Velocidad del viento: {weather.wind_speed} m/s")

        print("\nRecomendación de ropa:")
        print(recommendation)

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":  
    main()
