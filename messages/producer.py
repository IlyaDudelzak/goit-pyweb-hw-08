from models import Contact
from faker import Faker
import json
import pika

CONTACTS_AMOUNT = 10
QUEUE_NAME = "pyweb-08"

credentials = pika.PlainCredentials("xgztisfp", "yWkCVCo_JSUl8z-ofhF0NGxU0gpjneU3")
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='hawk.rmq.cloudamqp.com', virtual_host="xgztisfp", port=5672, credentials=credentials))
channel = connection.channel()

channel.exchange_declare(exchange='task_mock', exchange_type='direct')
channel.queue_declare(queue=QUEUE_NAME, durable=True)
channel.queue_bind(exchange='task_mock', queue=QUEUE_NAME)

if __name__ == '__main__':
    Contact.drop_collection()
    faker = Faker("ru_RU")
    contacts = []
    for i in range(CONTACTS_AMOUNT):
        contact = Contact(email=faker.email(), fullname=faker.name(), sent=False)
        contact.save()
        contacts.append(contact)
        message = {"contact_id": str(contact.id), "message": faker.text()}
        channel.basic_publish(exchange='', routing_key=QUEUE_NAME, body=json.dumps(message).encode())
        print(f"Sent {message['message']}")

    connection.close()

