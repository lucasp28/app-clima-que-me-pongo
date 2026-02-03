class ClothingAdvisor:

    def recommend(self, weather):
        temp = weather.feels_like
        wind = weather.wind_speed
        humidity = weather.humidity
        desc = weather.description.lower()

        advice = []

        # Recomendaciones basadas en la temperatura
        if temp < 0:
            advice.append("¡Hace mucho frío! Usa ropa abrigada, guantes y gorro.")
        elif temp < 10:
            advice.append("Hace mucho frío, usa abrigo pesado y bufanda.")
        elif temp < 18:
            advice.append("Clima fresco, llevate una camperita.")
        elif temp < 25:
            advice.append("Clima agradable, una remera y jeans están bien.")
        elif temp < 30:
            advice.append("Hace calor, usa ropa ligera como shorts y remera.")
        else:
            advice.append("¡Hace mucho calor! Ropa muy ligera, protector solar y mantenete hidratado.")


        # Recomendaciones basadas en viento, humedad y lluvia
        if wind > 20:
            advice.append("Viento fuerte. Considera usar una chaqueta resistente al viento.")

        if humidity > 80:
            advice.append("Alta humedad. Puede sentirse mas el calor.")

        if "lluvia" in desc or "rain" in desc:
            advice.append("Ojota que llueve. Lleva un paraguas o ropa impermeable.")

        
        # Retorna las recomendaciones como un string
        return "\n".join(advice)
    