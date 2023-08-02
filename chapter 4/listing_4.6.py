import asyncio
import aiohttp
from aiohttp import ClientSession
from book_asyncio_and_concurrency_in_Python.chapter_04 import fetch_status
from book_asyncio_and_concurrency_in_Python.util import async_timed


@async_timed()
async def main():
    async with ClientSession() as session:
        urls = ['https://example.com', 'python://example.com']
        requests = [fetch_status(session, url) for url in urls]
        status_codes = await asyncio.gather(*requests, return_exceptions=True)

        exceptions = [res for res in status_codes if isinstance(res, Exception)]
        successful_results = [res for res in status_codes if not isinstance(res, Exception)]
        print(f'Все результаты: {status_codes}')
        print(f'Завершились успешно: {successful_results}')
        print(f'Завершились с исключением: {exceptions}')

asyncio.run(main())