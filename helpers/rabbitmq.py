import pika

def use_rabbitmq(details):
  
  credentials = pika.PlainCredentials(details["user"], details["pass"])
  connection = pika.BlockingConnection(pika.ConnectionParameters(host=details["host"], credentials=credentials))
  channel = connection.channel()
  
  ex = details["exchange"]
  q = details["queue"]

  channel.queue_declare(queue=q)
  channel.exchange_declare(exchange=ex, exchange_type='topic')

  channel.queue_bind(exchange=ex, queue=q)
  channel.basic_publish(exchange=ex, routing_key=q, body=str(details["payload"]))

  connection.close()
  
