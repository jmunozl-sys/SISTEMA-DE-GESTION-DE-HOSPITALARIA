import requests
import os

def consultar_api_externa(parametro):
    # Obtener el Token desde variables de entorno por seguridad
    api_token = os.environ.get('API_KEY_EXTERNA')
    url = f"https://api.ejemplo.com/v1/consulta/{parametro}"
    
    headers = {
        "Authorization": f"Bearer {api_token}",
        "Content-Type": "application/json"
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=5)
        if response.status_code == 200:
            return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error al conectar con la API: {e}")
    
    return None