from __future__ import annotations

import json
from typing import Any, Awaitable, Callable, Dict, List, Optional

from aiokafka import AIOKafkaConsumer, AIOKafkaProducer

from app.core.config import get_settings

TOPICS = (
    "sheldra.interactions",
    "decision.trees",
    "sensor.readings",
    "vision.detections",
    "worker.profiles",
    "system.alerts",
)


class KafkaProducer:
    def __init__(self) -> None:
        self._producer: AIOKafkaProducer | None = None

    async def start(self) -> None:
        if self._producer is None:
            self._producer = AIOKafkaProducer(
                bootstrap_servers=get_settings().kafka_broker_url,
                value_serializer=lambda payload: json.dumps(payload).encode(),
            )
            await self._producer.start()

    async def stop(self) -> None:
        if self._producer is not None:
            await self._producer.stop()
            self._producer = None

    async def publish(self, topic: str, message: Dict[str, Any]) -> None:
        if self._producer is None:
            raise RuntimeError("Kafka producer has not started")
        await self._producer.send_and_wait(topic, message)


MessageHandler = Callable[[Dict[str, Any]], Awaitable[None]]


class KafkaConsumer:
    def __init__(self, topics: List[str], group_id: str) -> None:
        self._topics = topics
        self._group_id = group_id
        self._consumer: Optional[AIOKafkaConsumer] = None

    async def start(self) -> None:
        self._consumer = AIOKafkaConsumer(
            *self._topics,
            bootstrap_servers=get_settings().kafka_broker_url,
            group_id=self._group_id,
            value_deserializer=lambda value: json.loads(value.decode()),
        )
        await self._consumer.start()

    async def consume(self, handler: MessageHandler) -> None:
        if self._consumer is None:
            raise RuntimeError("Kafka consumer has not started")
        async for message in self._consumer:
            await handler(message.value)

    async def stop(self) -> None:
        if self._consumer is not None:
            await self._consumer.stop()
            self._consumer = None
