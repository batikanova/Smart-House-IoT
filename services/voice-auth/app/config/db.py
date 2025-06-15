import os
import psycopg2
from psycopg2 import pool



pg_pool = None


def get_db():
    global pg_pool
    return pg_pool.getconn()

def release_db(conn):
    global pg_pool
    pg_pool.putconn(conn)