import os

def generate_random_message():
    message = os.urandom(64)  # Генерируем случайное сообщение (64 байта)
    readable_message = message.hex()  # Преобразуем в шестнадцатеричную строку
    return readable_message

message = generate_random_message()
print(f"Сгенерированное сообщение: {message}")

