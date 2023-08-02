import asyncio

from book_asyncio_and_concurrency_in_Python.util import async_timed


@async_timed()
async def delay(delay_seconds: int) -> int:
    print(f'imma to sleep on {delay_seconds} seconds')
    await asyncio.sleep(delay_seconds)
    print(f'sleep within {delay_seconds} is over')
    return delay_seconds


@async_timed()
async def main():
    task_one = asyncio.create_task(delay(2))
    task_two = asyncio.create_task(delay(3))

    await task_one
    await task_two


asyncio.run(main())