import psycopg2
from config1 import load_config

config = load_config()

conn = psycopg2.connect(**config)

conn.set_client_encoding("UTF8")

print("CONNECTED SUCCESSFULLY")