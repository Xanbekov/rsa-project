from Crypto.Signature import pkcs1_15
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256

# Загрузка приватного ключа
private_key = RSA.import_key(open("private.pem").read())

# Генерация сообщения для подписи
message = "Это тестовое сообщение".encode('utf-8')  # Кодируем строку в байты с использованием UTF-8
hash_message = SHA256.new(message)

# Подпись сообщения
signature = pkcs1_15.new(private_key).sign(hash_message)

# Сохранение подписи в файл
with open("signature.bin", "wb") as f:
    f.write(signature)

print("Сообщение подписано!")


