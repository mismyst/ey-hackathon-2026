"""Create SHELDRA Kafka topics. Run after `docker compose up -d`."""
import asyncio

from aiokafka.admin import AIOKafkaAdminClient, NewTopic

from app.services.kafka import TOPICS


async def main() -> None:
    admin = AIOKafkaAdminClient(bootstrap_servers="localhost:29092")
    await admin.start()
    try:
        await admin.create_topics([NewTopic(topic, 1, 1) for topic in TOPICS])
    finally:
        await admin.close()


if __name__ == "__main__":
    asyncio.run(main())
