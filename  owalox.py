import requests
import random

# Генерация случайных данных (неэффективно для обхода защиты)
def generate_fake_data():
    username = f"user_{random.randint(1000, 9999)}"
    email = f"{username}@tempmail.com"
    return email, username

# Попытка регистрации (не работает без обхода CAPTCHA)
def register_account():
    email, username = generate_fake_data()
    
    url = "https://discord.com/api/v9/auth/register"
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
    }
    
    payload = {
        "email": email,
        "username": username,
        "password": "A$ecretPa$$w0rd",
        "consent": True,
        "fingerprint": None  # На практике требуется реальный fingerprint
    }
    
    try:
        response = requests.post(url, json=payload, headers=headers)
        print(f"Статус: {response.status_code}, Ответ: {response.text}")
    except Exception as e:
        print(f"Ошибка: {str(e)}")

register_account()