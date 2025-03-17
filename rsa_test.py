from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from Crypto.Random import get_random_bytes
import os

# Генерация ключей
def generate_keys():
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()

    with open("private.pem", "wb") as f:
        f.write(private_key)
    
    with open("public.pem", "wb") as f:
        f.write(public_key)

    print("Ключи успешно сгенерированы!")

# Подписание сообщения
def sign_message(message):
    # Загрузка приватного ключа
    with open("private.pem", "rb") as f:
        private_key = RSA.import_key(f.read())
    
    # Хеширование сообщения
    hash_obj = SHA256.new(message)
    
    # Подписание хеша
    signature = pkcs1_15.new(private_key).sign(hash_obj)
    
    # Сохранение подписи
    with open("signature.bin", "wb") as f:
        f.write(signature)

    print("Сообщение подписано и сохранено в 'signature.bin'.")

# Проверка подписи
def verify_signature(message):
    # Загрузка публичного ключа
    with open("public.pem", "rb") as f:
        public_key = RSA.import_key(f.read())

    # Загрузка подписи
    with open("signature.bin", "rb") as f:
        signature = f.read()

    # Хеширование сообщения
    hash_obj = SHA256.new(message)

    try:
        # Проверка подписи
        pkcs1_15.new(public_key).verify(hash_obj, signature)
        print("Подпись верна!")
    except (ValueError, TypeError):
        print("Подпись неверна.")

# Генерация случайного сообщения
def generate_random_message():
    message = get_random_bytes(256)
    print(f"Сгенерированное сообщение: {message.hex()}")

# Главная функция
def main():
    print("1. Генерация ключей...")
    generate_keys()  # Генерация ключей
    
    message = "Это тестовое сообщение".encode('utf-8')
    
    print("\n2. Подписание сообщения...")
    sign_message(message)  # Подписание сообщения
    
    print("\n3. Проверка подписи...")
    verify_signature(message)  # Проверка подписи
    
    print("\n4. Генерация случайного сообщения...")
    generate_random_message()  # Генерация случайного сообщения

if __name__ == "__main__":
    main()

