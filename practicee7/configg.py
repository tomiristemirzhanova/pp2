from configparser import ConfigParser
from pathlib import Path


def load_config(filename=None, section="postgresql"):
    parser = ConfigParser()

    if filename is None:
        filename = Path(__file__).resolve().parent / "database.ini"

    read_files = parser.read(filename)

    if not read_files:
        raise Exception(
            f"Config file not found: {filename}. Create database.ini from database.ini.example and fill in your credentials."
        )

    if not parser.has_section(section):
        raise Exception(f"Section '{section}' not found in the config file: {filename}")

    return {key: value for key, value in parser.items(section)}