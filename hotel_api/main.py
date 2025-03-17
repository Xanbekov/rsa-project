from fastapi import FastAPI
import psycopg2

app = FastAPI()

# Подключение к базе данных
conn = psycopg2.connect(
    dbname="hotel_db",
    user="hotel_admin",
    password="password123",
    host="localhost"
)

@app.get("/")
def home():
    return {"message": "Добро пожаловать в систему управления заявками отеля!"}

