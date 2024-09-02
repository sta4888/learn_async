import asyncio
from contextlib import contextmanager, asynccontextmanager

from redis import asyncio as aioredis


@contextmanager
def custom_open(filename, mode='w'):
    file_obj = open(filename, mode)
    yield file_obj
    file_obj.close()


@asynccontextmanager
async def redis_connection():
    try:
        redis = await aioredis.from_url('redis://localhost')
        yield redis
    finally:
        await redis.close()


async def main():
    async with redis_connection() as redis:
        await redis.set('course', 'asyncio')


asyncio.run(main())
