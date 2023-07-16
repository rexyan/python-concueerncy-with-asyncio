import asyncio
from asyncio import Lock
from util import delay


async def a(lock: Lock):
    print('等待 a 获取锁')
    async with lock:
        print('a 获取到了锁')
        await delay(2)
    print('a 释放了锁')


async def b(lock: Lock):
    print('等待 b 获取锁')
    async with lock:
        print('b 获取到了锁')
        await delay(2)
    print('b 释放了锁')


async def main():
    lock = Lock()
    await asyncio.gather(a(lock), b(lock))


asyncio.run(main())
