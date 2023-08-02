from aiohttp import ClientSession

from book_asyncio_and_concurrency_in_Python.util import async_timed


@async_timed()
async def fetch_status(session: ClientSession, url: str) -> int:
    async with session.get(url) as result:
        return result.status