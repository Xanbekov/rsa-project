import os
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from Crypto.Random import get_random_bytes

# Генерация ключей
def generate_keys():
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()

    with open("private.pem", "wb") as f:
        f.write(private_key)
    with open("public.pem", "wb") as f:
        f.write(public_key)

    print("Ключи успешно сгенерированы и сохранены в файлы private.pem и public.pem.")

# Подписание сообщения
def sign_message(message):
    with open("private.pem", "rb") as f:
        private_key = RSA.import_key(f.read())

    hash_obj = SHA256.new(message)
    signer = pkcs1_15.new(private_key)
    signature = signer.sign(hash_obj)

    with open("signature.bin", "wb") as f:
        f.write(signature)

    print("Сообщение подписано!")

# Проверка подписи
def verify_signature(message):
    with open("public.pem", "rb") as f:
        public_key = RSA.import_key(f.read())

    with open("signature.bin", "rb") as f:
        signature = f.read()

    hash_obj = SHA256.new(message)
    verifier = pkcs1_15.new(public_key)

    try:
        verifier.verify(hash_obj, signature)
        print("Подпись верна!")
    except (ValueError, TypeError):
        print("Подпись неверна!")

# Генерация случайного сообщения
def generate_random_message():
    message = get_random_bytes(128)
    print(f"Сгенерированное сообщение: {message.hex()}")
    return message

# Основная логика
if __name__ == "__main__":
    print("1. Генерация ключей...")
    generate_keys()

    print("\n2. Подписание сообщения...")
    message = "Это тестовое сообщение".encode('utf-8')
    sign_message(message)

    print("\n3. Проверка подписи...")
    verify_signature(message)

    print("\n4. Генерация случайного сообщения...")
    generate_random_message()

