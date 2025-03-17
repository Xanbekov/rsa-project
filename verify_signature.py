from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

# Загружаем публичный ключ
with open("public.pem", "rb") as f:
    public_key = RSA.import_key(f.read())

# Сообщение и подпись
message = "Это тестовое сообщение".encode('utf-8')
with open("signature.bin", "rb") as f:
    signature = f.read()

# Хеширование сообщения
hash_obj = SHA256.new(message)

# Верификация подписи
verifier = pkcs1_15.new(public_key)
try:
    verifier.verify(hash_obj, signature)
    print("Подпись верна!")
except (ValueError, TypeError):
    print("Подпись неверна!")

