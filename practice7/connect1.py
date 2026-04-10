import psycopg2
from config1 import load_config


def connect():
    """Connect to the PostgreSQL database server."""
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            print("Connected to PostgreSQL successfully!")
    except Exception as error:
        print("Connection error:", error)


if __name__ == "__main__":
    connect()