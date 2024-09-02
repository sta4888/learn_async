# pip install aiohttp
from time import time

# План
# 1. Asyncio фреймворк для создания событийных циклов
# 2. Пример простой асинхронной программы времен Python 3.4
# 3. Синтаксис Async/await на замену @asyncio.coroutine и yield from
# 4. Пример асинхронного скачивания файлов
###########################################################
# import asyncio
# from time import time
#
# @asyncio.coroutine
# def print_nums():
#     num = 1
#     while True:
#         print(num)
#         num += 1
#         yield from asyncio.sleep(.1)
#
# @asyncio.coroutine
# def print_time():
#     count = 0
#     while True:
#         if count % 3 == 0:
#             print("{} seconds".format(count))
#         count += 1
#         yield from asyncio.sleep(1)
#
# @asyncio.coroutine
# def main():
#     task1 = asyncio.ensure_future(print_nums())
#     task2 = asyncio.ensure_future(print_time())
#
#     yield from asyncio.gather(task1, task2)
#
#
# if __name__ == '__main__':
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(main())
#     loop.close()
###########################################################
# import asyncio
# from time import time
#
#
# async def print_nums():  # 3.5
#     num = 1
#     while True:
#         print(num)
#         num += 1
#         await asyncio.sleep(.1)  # 3.5
#
#
# async def print_time():  # 3.5
#     count = 0
#     while True:
#         if count % 3 == 0:
#             print("{} seconds".format(count))
#         count += 1
#         await asyncio.sleep(1)  # 3.5
#
#
# async def main():
#     task1 = asyncio.create_task(print_nums())  # 3.6
#     task2 = asyncio.create_task(print_time())
#
#     await asyncio.gather(task1, task2)
#
#
# if __name__ == '__main__':
#     # loop = asyncio.get_event_loop()
#     # loop.run_until_complete(main())
#     # loop.close()
#     asyncio.run(main())  # 3.7
###########################################################
# import requests
#
# # url = "https://loremflicker.com/320/240"
#
#
# def get_file(url):
#     r = requests.get(url)
#     return r
#
#
# def write_file(response):
#     filename = response.url.split("/")[-1]
#     with open(filename, 'wb') as f:
#         f.write(response.content)
#
#
# def main():
#     t0 = time()
#
#     url = "https://loremflickr.com/320/240"
#
#     for i in range(10):
#         write_file(get_file(url))
#
#     print(time() - t0)
#
#
# if __name__ == "__main__":
#     main() # 4.30

###########################################################
import asyncio  # предоставляет протокол для работы с tcp и udp
import aiohttp  # предоставляет протокол для http (лучше все запросы делать через созданную сессию)


def write_image(data):
    filename = f"file-{str(int(time() * 1000))}.jpeg"
    with open(filename, "wb") as f:
        f.write(data)


async def fetch_content(url, session):  # корутина
    async with session.get(url,
                           allow_redirects=True) as response:  # с сессиями мы обычно работаем через контекстный менеджер
        data = await response.read()
        write_image(data)  # здесь нужно посмотретьмодули для ассинхронной записи файлов


async def main2():
    url = 'https://loremflickr.com/320/240'
    tasks = []
    async with aiohttp.ClientSession() as session:
        for i in range(10):
            task = asyncio.create_task(fetch_content(url, session))
            tasks.append(task)

        await asyncio.gather(*tasks)


if __name__ == '__main__':
    t0 = time()
    asyncio.run(main2())
    print(time() - t0)  # .5
