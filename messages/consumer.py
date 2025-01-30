from models import Contact, ObjectId, connect
from connect import channel, connection
import json

QUEUE_NAME = "pyweb-08"

def main():
    channel.queue_declare(queue=QUEUE_NAME, durable=True)

    def callback(ch, method, properties, body):
        try:
            message = json.loads(body)
            contact = Contact.objects(id=ObjectId(message["contact_id"]))[0]
            print(f"Sent message to {contact.fullname}({contact.email}): {message["message"]}!")  
        except json.decoder.JSONDecodeError:
            print("Error parsing message")

    channel.basic_consume(queue=QUEUE_NAME, on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        exit(0)