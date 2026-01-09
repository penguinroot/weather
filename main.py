import requests

def obtenir_meteo(ville):
    geo_url = "https://geocoding-api.open-meteo.com/v1/search"
    geo_params = {"name": ville, "count": 1}
    resultat_geo = requests.get(geo_url, params=geo_params).json()

    if "results" not in resultat_geo:
        print("Désolé, je n'ai pas trouvé cette ville.")
        return

    latitude = resultat_geo["results"][0]["latitude"]
    longitude = resultat_geo["results"][0]["longitude"]

    meteo_url = "https://api.open-meteo.com/v1/forecast"
    meteo_params = {
        "latitude": latitude,
        "longitude": longitude,
        "current_weather": True,
        "timezone": "auto"
    }
    resultat_meteo = requests.get(meteo_url, params=meteo_params).json()

    if "current_weather" in resultat_meteo:
        meteo = resultat_meteo["current_weather"]
        print(f"Météo actuelle à {ville} :")
        print(f"Température : {meteo['temperature']}°C")
        print(f"Vitesse du vent : {meteo['windspeed']} km/h")
        print(f"Direction du vent : {meteo['winddirection']}°")
        print(f"Heure : {meteo['time']}")
    else:
        print("Impossible de récupérer les données météo pour le moment.")

if __name__ == "__main__":
    ville = input("Entrez le nom de votre ville : ")
    obtenir_meteo(ville)
