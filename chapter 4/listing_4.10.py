import asyncio
import aiohttp

from aiohttp import ClientSession
from book_asyncio_and_concurrency_in_Python.util import async_timed
from book_asyncio_and_concurrency_in_Python.chapter_04 import fetch_status


@async_timed()
async def main():
    async with ClientSession() as session:
        fetchers = [
            asyncio.create_task(fetch_status(session, 'https://example.com')),
            asyncio.create_task(fetch_status(session, 'https://example.com'))
        ]

        done, pending = await asyncio.wait(fetchers)

        print(f'Число завершившихся задач: {len(done)}')
        print(f'Число ожидающих задач: {len(pending)}')

        for done_task in done:
            result = await done_task
            print(result)
            

asyncio.run(main())