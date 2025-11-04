import aio_pika
import json
import os

RABBITMQ_URL = os.getenv("RABBITMQ_URL", "amqp://user:password@rabbitmq:5672/")

async def publish_task(task: dict):
    connection = await aio_pika.connect_robust(RABBITMQ_URL)
    async with connection:
        channel = await connection.channel()
        queue = await channel.declare_queue("compression_tasks", durable=True)
        message = aio_pika.Message(body=json.dumps(task).encode())
        await channel.default_exchange.publish(message, routing_key=queue.name)
