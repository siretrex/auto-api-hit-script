import requests
import time

API_URL = "https://chro-api.onrender.com/login"  

PAYLOAD = {
    "email": "ritik.k@example.com",
    "password": "SecurePass123!"
}

def send_request():
    try:
        response = requests.post(API_URL, json=PAYLOAD)
        print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Status: {response.status_code}")
        print("Response:", response.text)
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    send_request()
