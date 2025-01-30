from dotenv import dotenv_values
from mongoengine import connect

config = dotenv_values("../.env")

domain = config["MONGO_HOST"]
mongo_user = config["MONGO_USER"]
mongo_pass = config["MONGO_PASS"]
db_name = config["MONGO_DB_NAME"]

connect(host=f"mongodb+srv://{mongo_user}:{mongo_pass}@{domain}/?retryWrites=true&w=majority&appName={db_name}", ssl=True, alias='default')