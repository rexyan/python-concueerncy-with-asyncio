import asyncio

import aiohttp

from util import async_timed, fetch_status


@async_timed()
async def main():
    async with aiohttp.ClientSession() as session:
        urls = ['https://baidu.com' for _ in range(1000)]
        status_codes = [await fetch_status(session, url) for url in urls]
        print(status_codes)


asyncio.run(main())
