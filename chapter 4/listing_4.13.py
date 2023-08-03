import asyncio
import aiohttp
from book_asyncio_and_concurrency_in_Python.util import async_timed
from book_asyncio_and_concurrency_in_Python.chapter_04 import fetch_status


@async_timed()
async def main():
    async with aiohttp.ClientSession() as session:
        url = 'https://example.com'

        fetchers = [
            asyncio.create_task(fetch_status(session, url)),
            asyncio.create_task(fetch_status(session, url)),
            asyncio.create_task(fetch_status(session, url)),
        ]

        done, pending = await asyncio.wait(fetchers, return_when=asyncio.FIRST_COMPLETED)

        print(f'Число завершившихся задач: {len(done)}')
        print(f'Число ожидающих задач: {len(pending)}')

        for task_done in done:
            print(await task_done)


asyncio.run(main())
