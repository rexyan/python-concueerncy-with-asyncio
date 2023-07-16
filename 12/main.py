import asyncio
from util import delay


async def create_tasks_no_sleep():
    task1 = asyncio.create_task(delay(1))
    task2 = asyncio.create_task(delay(2))
    # 没有使用 asyncio.sleep(0) 的时候，会先打印下面的 "获取到任务：" 然后 gather 在执行任务
    print("获取到任务：")
    await asyncio.gather(task1, task2)


async def create_tasks_sleep():
    task1 = asyncio.create_task(delay(1))
    await asyncio.sleep(0)
    task2 = asyncio.create_task(delay(2))
    await asyncio.sleep(0)
    # 使用 asyncio.sleep(0) 的时候，会先执行上面的任务，然后在打印 "获取到任务："
    print("获取到任务：")
    await asyncio.gather(task1, task2)


async def main():
    print('--- 没有使用 asyncio.sleep(0) ---')
    await create_tasks_no_sleep()
    print('--- 使用 asyncio.sleep(0) ---')
    await create_tasks_sleep()


asyncio.run(main())
