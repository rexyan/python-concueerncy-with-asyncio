import asyncio

import aiohttp

from util import fetch_status, async_timed


@async_timed()
async def main():
    async with aiohttp.ClientSession() as session:
        urls = ['python://example.com', 'https://baidu.com']
        tasks = [fetch_status(session, url) for url in urls]
        status_codes = await asyncio.gather(*tasks)
        print(status_codes)


asyncio.run(main())
