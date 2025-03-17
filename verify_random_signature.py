from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

# Загружаем публичный ключ
with open("public.pem", "rb") as f:
    public_key = RSA.import_key(f.read())

# Загружаем случайное сообщение и подпись
with open("random_message.bin", "rb") as f:
    random_message = f.read()

with open("random_signature.bin", "rb") as f:
    signature = f.read()

# Хеширование сообщения
hash_obj = SHA256.new(random_message)

# Верификация подписи
verifier = pkcs1_15.new(public_key)
try:
    verifier.verify(hash_obj, signature)
    print("Подпись верна для случайного сообщения!")
except (ValueError, TypeError):
    print("Подпись неверна для случайного сообщения!")

