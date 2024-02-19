import pika

# Define callback function to handle incoming messages
def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)

# Establish a connection to RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare the queue
channel.queue_declare(queue='hello')

# Set up a consumer to receive messages from the queue
channel.basic_consume(queue='hello',
                      on_message_callback=callback,
                      auto_ack=True)

print(' [*] Waiting for messages. To exit, press CTRL+C')
channel.start_consuming()
