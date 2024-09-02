import asyncio


async def greet(timeout):
    await asyncio.sleep(timeout)
    return 'Hello world'


async def main():
    long_task = asyncio.create_task(greet(5))

    try:
        result = await asyncio.wait_for(
            asyncio.shield(long_task),
            timeout=2
        )
    except asyncio.TimeoutError:
        print('The long task cancelled')
        result = await long_task
        
        print(result)



asyncio.run(main())
