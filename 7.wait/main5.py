import asyncio

import aiohttp

from util import fetch_status


async def main():
    async with aiohttp.ClientSession() as session:
        api_a = fetch_status(session, 'https://www.baidu.com')
        api_b = fetch_status(session, 'https://www.baidu.com', delay=2)

        done, pending = await asyncio.wait([api_a, api_b], timeout=1)

        for task in pending:
            if task is api_b:
                # 期待结果为取消 api_b，但是并没有执行
                print('API B too slow, cancelling')
                task.cancel()


asyncio.run(main())
