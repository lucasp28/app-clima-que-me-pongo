from dataclasses import dataclass

# Esta clase no piensa, solo es un contenedor de datos
@dataclass
class Weather:
    temperature: float
    feels_like: float
    humidity: int
    wind_speed: float
    description: str