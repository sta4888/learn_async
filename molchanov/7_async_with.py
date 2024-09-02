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
        print(f'{url}: {html[:20]}')


async def main():
    res1 = asyncio.create_task(check('https://facebook.com'))
    res2 = asyncio.create_task(check('https://youtube.com'))
    res3 = asyncio.create_task(check('https://google.com'))

    print(await res1)
    print(await res2)
    print(await res3)

asyncio.run(main())
