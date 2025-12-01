# Importación de librerías necesarias
from xmlrpc.client import boolean
import requests

# Parámetros para la solicitud a la API de Open Trivia Database
# amount: número de preguntas a obtener
# type: tipo de preguntas (boolean = verdadero/falso)
parameters = {
    "amount":10,
    "type": "boolean"
}

# Realizar solicitud GET a la API de Open Trivia Database
response = requests.get("https://opentdb.com/api.php?amount=10&type=boolean", params=parameters)
# Verificar que la solicitud fue exitosa (lanza excepción si hay error)
response.raise_for_status()
# Convertir la respuesta JSON a un diccionario de Python
data = response.json()

# Extraer la lista de preguntas del resultado de la API
question_data = data["results"]


