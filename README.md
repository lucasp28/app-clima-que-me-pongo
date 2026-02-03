# App de Clima y Recomendación de Ropa

Esta es mi primera app en Python que consulta el clima de una ciudad usando la API de OpenWeatherMap y recomienda qué ropa usar según la temperatura, sensación térmica, viento, humedad y lluvia.

---

## Características

- Consulta el clima actual de cualquier ciudad.  
- Muestra:
  - Temperatura
  - Sensación térmica
  - Humedad
  - Viento
  - Estado del clima (cielo claro, lluvia, nublado, etc.)
- Recomendación de ropa según los datos del clima.  
- Manejo de errores: ciudad inexistente, problemas de conexión o API caída.

---

## Requisitos

- Python 3.8 o superior  
- Librerías:
  - `requests`

---

## Instalación

1. Clonar el repositorio:

```bash
git clone https://github.com/TU_USUARIO/mi_app_clima.git
cd mi_app_clima
```

2. Instalar dependencias:

```bash
pip install -r requirements.txt
```

3. Crear cuenta en [OpenWeatherMap](https://openweathermap.org) y obtener tu API Key.

4. Configurar la variable de entorno en Windows (PowerShell o CMD):
```bash
setx OPENWEATHER_API_KEY "TU_API_KEY_AQUI"
```

5. Ejecutar la app:
```bash
python main.py
```

---

# Estructura del proyecto

```
app-clima-que-me-pongo/
├── main.py                   # Archivo principal
├── config.py                 # Configuración y API Key (no subir a GitHub, crear config_example.py)
├── models/                   # Clases de datos
│   └── weather.py
├── services/                 # Servicio que consulta la API
│   └── weather_service.py
├── logic/                    # Lógica de recomendación de ropa
│   └── clothing_advisor.py
├── requirements.txt          # Librerías necesarias
└── README.md                 # Este archivo
```





