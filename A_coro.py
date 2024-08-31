import asyncio


async def cpro1(duration):
    print("Starting my_coroutine 1")
    await asyncio.sleep(duration)
    print("Finishing my_coroutine 1")
    return "Result"


async def cpro2(duration):
    print("Starting my_coroutine 2")
    await asyncio.sleep(duration)
    print("Finishing my_coroutine 2")
    return "Result"


async def main():
    result1, result2 = await asyncio.gather(cpro1(2), cpro2(1))
    print(f"Result1: {result1}")
    print(f"Result2: {result2}")


if __name__ == '__main__':
    asyncio.run(main())
