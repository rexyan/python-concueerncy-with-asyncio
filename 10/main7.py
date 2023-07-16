import asyncio
from asyncio import Condition


async def do_work(condition: Condition):
    while True:
        print('do_work 等待获取条件锁...')
        async with condition:
            print('获取到锁，等待事件触发...')
            await condition.wait()
            print('事件被触发，正在执行...')
            await asyncio.sleep(1)
        print('do_work 工作结束，释放锁.')


async def fire_event(condition: Condition):
    while True:
        await asyncio.sleep(5)
        print('fire_event 等待获取条件锁...')
        async with condition:
            print('获取到锁，通知所有开始工作.')
            condition.notify_all()
        print('fire_event 工作结束，释放锁.')


async def main():
    condition = Condition()

    asyncio.create_task(fire_event(condition))
    await asyncio.gather(do_work(condition), do_work(condition))


asyncio.run(main())
"""
do_work 等待获取条件锁...
获取到锁，等待事件触发...
do_work 等待获取条件锁...
获取到锁，等待事件触发...
fire_event 等待获取条件锁...
获取到锁，通知所有开始工作.
fire_event 工作结束，释放锁.
事件被触发，正在执行...
do_work 工作结束，释放锁.
"""