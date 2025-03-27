import requests
import json

# URL de la API (asegúrate de que coincida con la dirección y puerto correctos)
url = "http://127.0.0.1:5000/predict"

# Datos que se enviarán a la API
data = {
    "area": 13000,
    "bedrooms": 15,
    "bathrooms": 11,
    "stories": 11,
    "mainroad": 1,
    "guestroom": 0,
    "basement": 0,
    "hotwaterheating": 0,
    "airconditioning": 0,
    "parking": 5,
    "prefarea": 0,
    "furnishingstatus_furnished": 0,
    "furnishingstatus_semi-furnished": 0,
    "furnishingstatus_unfurnished": 1
}


# Realizar la solicitud POST
try:
    # Enviar los datos a la API
    response = requests.post(url, json=data)

    # Verificar si la solicitud fue exitosa
    if response.status_code == 200:
        print("Respuesta de la API:")
        print(response.json())  # Mostrar la respuesta en formato JSON
    else:
        print(f"Error: Código de estado {response.status_code}")
        print(response.text)  # Mostrar el mensaje de error si lo hay
except Exception as e:
    print(f"Error al conectar con la API: {e}")
