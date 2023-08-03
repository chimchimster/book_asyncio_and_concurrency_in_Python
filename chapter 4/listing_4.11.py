import asyncio
import logging

import aiohttp

from book_asyncio_and_concurrency_in_Python.util import async_timed
from book_asyncio_and_concurrency_in_Python.chapter_04 import fetch_status

@async_timed()
async def main():
    async with aiohttp.ClientSession() as session:
        good_request = fetch_status(session, 'https://example.com')
        bad_request = fetch_status(session, 'python://bad')

        fetchers = [
            asyncio.create_task(good_request),
            asyncio.create_task(bad_request)
        ]

        done, pending = await asyncio.wait(fetchers)

        print(f'Число завершившихся задач: {len(done)}')
        print(f'Число ожидающих задач: {len(pending)}')
        
        for done_task in done:
            if done_task.exception() is None:
                print(done_task.result())
            else:
                logging.error('При выполнении запроса возникло исключение', exc_info=done_task.exception())


asyncio.run(main())