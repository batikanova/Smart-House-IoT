from app import createApp
from dotenv import load_dotenv
import psycopg2
import os

app = createApp()
load_dotenv()

pg_pool = psycopg2.pool.SimpleConnectionPool(
    1,                     # min bağlantı
    10,                    # max bağlantı
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
    database=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASS")       # env'den alınan bağlantı bilgisi
)
if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=1000)