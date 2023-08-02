import asyncio
from book_asyncio_and_concurrency_in_Python.util import delay


async def main():
    delay_task = asyncio.create_task(delay(2))

    try:
        result = await asyncio.wait_for(delay_task, timeout=1)
        print(result)
    except asyncio.exceptions.TimeoutError:
        print('Timeout!')
        print(f'Has task been canceled? {delay_task.cancelled()}')


asyncio.run(main())