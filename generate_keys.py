from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes

# Генерация RSA ключей
key = RSA.generate(2048)

# Сохранение приватного ключа
with open("private.pem", "wb") as private_file:
    private_file.write(key.export_key())

# Сохранение публичного ключа
with open("public.pem", "wb") as public_file:
    public_file.write(key.publickey().export_key())

print("Ключи успешно сгенерированы!")


