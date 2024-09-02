import asyncio


async def coro():
    return 1


async def main():
    task = asyncio.create_task(coro())

    await task
    print(task.cancelled())


asyncio.run(main())
