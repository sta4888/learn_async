import asyncio

from fastapi import FastAPI


app = FastAPI()
lock = asyncio.Lock()
count = 0


@app.get('/')
async def main():
    global count

    async with lock:
        count += 1

    return {'count': count}

@app.get('/hello')
async def greet():
    return {'msg': 'Hello world'}
