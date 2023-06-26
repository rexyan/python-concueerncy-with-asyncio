"""同时运行多个任务"""
import asyncio
import time

from util import delay


async def main():
    """
    启动了三个任务，每个任务花费3秒钟来完成。
    但总时长大约花费 3s 左右
    :return:
    """
    a = asyncio.create_task(delay(3))  # 每次调用create_task都会立即返回
    b = asyncio.create_task(delay(3))
    c = asyncio.create_task(delay(3))

    await a  # 创建任务后第一次遇到 await 语句时，任何待处理的任务都会随着 await 触发事件循环的迭代而运行。
    await b
    await c


start_time = time.perf_counter()
asyncio.run(main())
print(f"运行时长:{time.perf_counter() - start_time}")  # 运行时长:3.002205125999808
