import asyncio
import aiohttp
from aiohttp import ClientSession

from util import async_timed


@async_timed()
async def request(session: ClientSession, url: str, delay: int = 0) -> int:
    await asyncio.sleep(delay)
    async with session.get(url) as result:
        return result.status


@async_timed()
async def main():
    async with aiohttp.ClientSession() as session:
        fetchers = [
            request(session, 'https://baidu.com', 1),
            request(session, 'https://baidu.com', 1),
            request(session, 'https://baidu.com', 5)
        ]

        # 设置超时时间为 2s
        for done_task in asyncio.as_completed(fetchers, timeout=2):
            try:
                result = await done_task
                print(result)
            except asyncio.TimeoutError:
                print('获取到一个超时错误!')

        for task in asyncio.tasks.all_tasks():
            print(task)

asyncio.run(main())
