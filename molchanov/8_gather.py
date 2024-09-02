import asyncio
import aiohttp



class WriteToFile:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        self.file_object = open(self.filename, 'w')
        return self.file_object

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file_object:
            self.file_object.close()



class AsyncSession:
    def __init__(self, url):
        self._url = url

    async def __aenter__(self):
        self.session = aiohttp.ClientSession()
        response = await self.session.get(self._url)
        return response

    async def __aexit__(self, exc_type, exc_value, traceback):
        await self.session.close()


async def check(url):
    async with AsyncSession(url) as response:
        html = await response.text()
        return f'{url}: {html[:20]}'


class ServerError(Exception):
    def __init__(self, message):
        self._message = message

    def __str__(self):
        return self._message


async def server_returns_error():
    await asyncio.sleep(2)
    raise ServerError('Failed to get data')


async def main():

    urls = [
        'https://facebook.com',
        'https://youtube.com',
        'https://google.com',
    ]

    group1 = asyncio.gather(
        check('https://facebook.com'),
        check('https://youtube.com')
    )

    group2 = asyncio.gather(
        check('https://google.com'),
        check('https://youtube.com')
    )

    groups = asyncio.gather(group1, group2)

    results = await groups

    # coros = [check(url) for url in urls]
    #
    # for coro in asyncio.as_completed(coros):
    #     result = await coro
    #     print(result)

    # results = await asyncio.gather(
    #     *coros,
    #     # server_returns_error(),
    #     return_exceptions=True
    # )
    #
    # # results = await asyncio.gather(*[check(url) for url in urls])
    #
    for result in results:
        print(result)



asyncio.run(main())
