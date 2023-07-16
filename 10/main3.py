import asyncio
from asyncio import Semaphore


async def operation(semaphore: Semaphore):
    print('等待获取信号量...')
    async with semaphore:
        print('获取到信号量!')
        await asyncio.sleep(2)
    print('释放信号量!')


async def main():
    semaphore = Semaphore(2)
    await asyncio.gather(*[operation(semaphore) for _ in range(4)])


asyncio.run(main())
