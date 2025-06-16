from app import createApp
import psycopg2
import os

app = createApp()


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=1000)