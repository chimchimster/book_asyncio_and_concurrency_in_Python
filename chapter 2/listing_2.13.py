import asyncio
from book_asyncio_and_concurrency_in_Python.util import delay


async def main():
    task = asyncio.create_task(delay(10))

    try:
        result = await asyncio.wait_for(asyncio.shield(task), 5)
        print(result)
    except asyncio.exceptions.TimeoutError:
        print('Task took longer than 5 seconds, soon its gonna over')
        result = await task
        print(result)

asyncio.run(main())