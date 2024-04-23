import time
import requests

def send_request():
    url = ""  # Inserisci l'URL al quale inviare la richiesta

    try:
        response = requests.get(url)
        print(f"Request sent. Response: {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

def keep_service_online():
    while True:
        send_request()
        time.sleep(10)  # Attendi 10 secondi tra le richieste

if __name__ == "__main__":
    keep_service_online()