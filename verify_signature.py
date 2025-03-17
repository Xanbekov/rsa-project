from Crypto.Signature import pkcs1_15
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256

# Загрузка публичного ключа
public_key = RSA.import_key(open("public.pem").read())

# Генерация сообщения для проверки подписи
message = "Это тестовое сообщение".encode('utf-8')  # Кодируем строку в байты с использованием UTF-8
hash_message = SHA256.new(message)

# Загрузка подписи из файла
with open("signature.bin", "rb") as f:
    signature = f.read()

# Проверка подписи
try:
    pkcs1_15.new(public_key).verify(hash_message, signature)
    print("Подпись верна!")
except (ValueError, TypeError):
    print("Подпись неверна!")

