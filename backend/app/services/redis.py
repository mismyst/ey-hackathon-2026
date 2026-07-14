from __future__ import annotations

from typing import Optional

from redis.asyncio import ConnectionPool, Redis

from app.core.config import get_settings


class RedisManager:
    """Owns one async Redis connection pool for the application lifecycle."""

    def __init__(self) -> None:
        self._pool: Optional[ConnectionPool] = None
        self.client: Optional[Redis] = None

    async def connect(self) -> None:
        if self.client is None:
            self._pool = ConnectionPool.from_url(get_settings().redis_url, decode_responses=True)
            self.client = Redis(connection_pool=self._pool)

    async def disconnect(self) -> None:
        if self.client is not None:
            await self.client.aclose()
            self.client = None
        if self._pool is not None:
            await self._pool.aclose()
            self._pool = None

    async def ping(self) -> bool:
        if self.client is None:
            return False
        return bool(await self.client.ping())


redis_manager = RedisManager()
