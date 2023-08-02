import asyncio
from book_asyncio_and_concurrency_in_Python.util import delay


def call_later():
    print('I will be called in nearest time!')


async def main():
    loop = asyncio.get_running_loop()
    loop.call_soon(call_later)
    await delay(1)


asyncio.run(main(), debug=True)