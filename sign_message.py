from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes

# Загрузка приватного ключа
with open("private.pem", "rb") as f:
    private_key = RSA.import_key(f.read())

# Сообщение для подписи
message = "Это тестовое сообщение".encode('utf-8')

# Хэширование сообщения
hash_obj = SHA256.new(message)

# Подпись сообщения
signer = pkcs1_15.new(private_key)
signature = signer.sign(hash_obj)

# Сохранение подписи в файл
with open("signature.bin", "wb") as f:
    f.write(signature)

print("Сообщение подписано!")

