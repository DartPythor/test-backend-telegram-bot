import environ
from dotenv import load_dotenv


env = environ.Env()
environ.Env.read_env()
load_dotenv()

BASE_URL_SERVICE = env(
    "BASE_URL_SERVICE",
    default="http://localhost:8000",
    cast=str,
)

TOKEN_BOT = env(
    "TOKEN_BOT",
    cast=str,
)
