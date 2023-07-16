import asyncio

import aiohttp

from util import async_timed, fetch_status


@async_timed()
async def main():
    async with aiohttp.ClientSession() as session:
        url = 'https://www.baidu.com'
        pending = [
            asyncio.create_task(fetch_status(session, url)),
            asyncio.create_task(fetch_status(session, url)),
            asyncio.create_task(fetch_status(session, url, delay=3))
        ]

        while pending:
            done, pending = await asyncio.wait(pending, return_when=asyncio.FIRST_COMPLETED)

            print(f'完成任务数量: {len(done)}')
            print(f'阻塞任务数量: {len(pending)}')

            for done_task in done:
                print(await done_task)


asyncio.run(main())
