import asyncio
from asyncio import Semaphore
from aiohttp import ClientSession


async def get_url(url: str, session: ClientSession, semaphore: Semaphore):
    print('等待获取信号量...')
    async with semaphore:
        print('获取到信号量，请求中...')
        response = await session.get(url)
        print('请求完成')
        return response.status


async def main():
    semaphore = Semaphore(10)
    async with ClientSession() as session:
        tasks = [get_url('https://www.baidu.com', session, semaphore) for _ in range(1000)]
        await asyncio.gather(*tasks)


asyncio.run(main())
