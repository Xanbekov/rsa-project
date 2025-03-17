from Crypto.PublicKey import RSA

def generate_keys():
    # Генерация RSA ключей
    key = RSA.generate(2048)
    
    # Сохранение приватного ключа в файл
    with open("private.pem", "wb") as private_file:
        private_file.write(key.export_key())
    
    # Сохранение публичного ключа в файл
    with open("public.pem", "wb") as public_file:
        public_file.write(key.publickey().export_key())
    
    print("Ключи успешно сгенерированы и сохранены в файлы private.pem и public.pem.")

# Вызов функции для генерации ключей
generate_keys()

