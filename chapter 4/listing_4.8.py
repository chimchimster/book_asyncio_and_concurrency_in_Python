import asyncio
import aiohttp
from aiohttp import ClientSession
from book_asyncio_and_concurrency_in_Python.util import async_timed
from book_asyncio_and_concurrency_in_Python.chapter_04 import fetch_status


@async_timed()
async def main():
    async with ClientSession() as session:
        fetchers = [fetch_status(session, 'https://www.example.com', 1),
                    fetch_status(session, 'https://www.example.com', 1),
                    fetch_status(session, 'https://www.example.com', 10),
                    ]

        for finished_task in asyncio.as_completed(fetchers):
            print(await finished_task)


asyncio.run(main())
