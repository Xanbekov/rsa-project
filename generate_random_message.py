import os

# Генерация случайного сообщения
random_message = os.urandom(32)  # 32 байта случайных данных

# Сохраняем сообщение в файл
with open("random_message.bin", "wb") as f:
    f.write(random_message)

print("Случайное сообщение сгенерировано!")

