import asyncio
import aio_pika
import json
import time
import os

RABBITMQ_URL = os.getenv("RABBITMQ_URL", "amqp://user:password@rabbitmq:5672/")

async def handle_message(message: aio_pika.IncomingMessage):
    async with message.process():
        data = json.loads(message.body)
        print(f"Processing task {data['task_id']} for file {data['file_path']}")
        time.sleep(3)
        print(f"Task {data['task_id']} completed")

async def main():
    connection = await aio_pika.connect_robust(RABBITMQ_URL)
    channel = await connection.channel()
    queue = await channel.declare_queue("compression_tasks", durable=True)
    await queue.consume(handle_message)
    print("Worker started. Waiting for tasks...")
    await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())
