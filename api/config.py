from os import getenv

DEBUG = getenv("DEBUG") == "True"
DB_CONNECTION_STRING = getenv("DB_CONNECTION_STRING") or ""
