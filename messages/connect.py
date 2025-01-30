from dotenv import dotenv_values
from mongoengine import connect
import pika

config = dotenv_values("../.env")

MONGODB_HOST=config["MONGODB_HOST"]
MONGODB_USER=config["MONGODB_USER"]
MONGODB_PASS=config["MONGODB_PASS"]
MONGODB_NAME=config["MONGODB_NAME"]

RABBITMQ_HOST=config["RABBITMQ_HOST"]
RABBITMQ_USER=config["RABBITMQ_USER"]
RABBITMQ_PASS=config["RABBITMQ_PASS"]
RABBITMQ_PORT=config["RABBITMQ_PORT"]

connect(host=f"mongodb+srv://{MONGODB_USER}:{MONGODB_PASS}@{MONGODB_HOST}/?retryWrites=true&w=majority&appName={MONGODB_NAME}", ssl=True, alias='default')

credentials = pika.PlainCredentials(RABBITMQ_USER, RABBITMQ_PASS)
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host=RABBITMQ_HOST, virtual_host=RABBITMQ_USER, port=RABBITMQ_PORT, credentials=credentials))
channel = connection.channel()