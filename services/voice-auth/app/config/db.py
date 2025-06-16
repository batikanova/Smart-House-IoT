import os
import psycopg2
from psycopg2 import pool
from dotenv import load_dotenv

load_dotenv()


print("PostgreSQL bağlantısı kuruluyor...", os.getenv("DB_HOST"))
pgPool = psycopg2.pool.SimpleConnectionPool(
    1,                     # min bağlantı
    10,                    # max bağlantı
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
    database=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD")       # env'den alınan bağlantı bilgisi
)

def getDB():
    return pgPool.getconn()

def releaseDB(conn):
    pgPool.putconn(conn)