import asyncio
import requests
from book_asyncio_and_concurrency_in_Python.util import async_timed


@async_timed()
async def get_example_status() -> int:
    return requests.get('http://www.example.com').status_code


@async_timed()
async def main():
    task_1 = asyncio.create_task(get_example_status())
    task_2 = asyncio.create_task(get_example_status())
    task_3 = asyncio.create_task(get_example_status())

    await task_1
    await task_2
    await task_3


asyncio.run(main())