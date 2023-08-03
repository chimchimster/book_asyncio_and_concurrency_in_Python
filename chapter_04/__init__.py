import asyncio

from aiohttp import ClientSession

from book_asyncio_and_concurrency_in_Python.util import async_timed


@async_timed()
async def fetch_status(session: ClientSession, url: str, delay: int = 0) -> int:
    await asyncio.sleep(delay)
    async with session.get(url) as result:
        return result.status