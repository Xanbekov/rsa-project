from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

# Загружаем приватный ключ
with open("private.pem", "rb") as f:
    private_key = RSA.import_key(f.read())

# Загружаем случайное сообщение
with open("random_message.bin", "rb") as f:
    random_message = f.read()

# Хеширование сообщения
hash_obj = SHA256.new(random_message)

# Подписание сообщения
signer = pkcs1_15.new(private_key)
signature = signer.sign(hash_obj)

# Сохранение подписи в файл
with open("random_signature.bin", "wb") as f:
    f.write(signature)

print("Случайное сообщение подписано!")

