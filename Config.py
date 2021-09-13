from os import getenv
from dotenv import load_dotenv

load_dotenv()

ALIVE_PIC = getenv("ALIVE_PIC", "https://telegra.ph/file/0c113b325fe639b09a2d5.jpg")
STRING = getenv("STRING")
STRING2 = getenv("STRING2")
STRING3 = getenv("STRING3")
STRING4 = getenv("STRING4")
STRING5 = getenv("STRING5")
STRING6 = getenv("STRING6")
STRING7 = getenv("STRING7")
STRING8 = getenv("STRING8")
STRING9 = getenv("STRING9")
STRING10 = getenv("STRING10")
API_ID = getenv("API_ID")
API_HASH = getenv("API_HASH")
BIO_MESSAGE = getenv("BIO")
SUDO = list(map(int, getenv("SUDO").split()))
