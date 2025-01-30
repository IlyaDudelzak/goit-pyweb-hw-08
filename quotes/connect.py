from dotenv import dotenv_values
from mongoengine import connect

config = dotenv_values("../.env")

MONGODB_HOST=config["MONGODB_HOST"]
MONGODB_USER=config["MONGODB_USER"]
MONGODB_PASS=config["MONGODB_PASS"]
MONGODB_NAME=config["MONGODB_NAME"]

connect(host=f"mongodb+srv://{MONGODB_USER}:{MONGODB_PASS}@{MONGODB_HOST}/?retryWrites=true&w=majority&appName={MONGODB_NAME}", ssl=True, alias='default')