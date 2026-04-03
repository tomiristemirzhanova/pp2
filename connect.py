import psycopg2
from config import load_config


def get_connection():
    """Create and return a PostgreSQL connection."""
    config = load_config()
    return psycopg2.connect(**config)