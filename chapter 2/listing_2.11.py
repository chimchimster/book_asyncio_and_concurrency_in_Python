import asyncio
from asyncio import CancelledError
from book_asyncio_and_concurrency_in_Python.util import delay

async def main():
    long_task = asyncio.create_task(delay(10))

    seconds_elapsed = 0

    while not long_task.done():
        print('Task is in progress, next check after one second.')
        await asyncio.sleep(1)

        seconds_elapsed += 1

        if seconds_elapsed == 5:
            long_task.cancel()

    try:
        await long_task
    except CancelledError:
        print('Taks has been canceled!')


asyncio.run(main())