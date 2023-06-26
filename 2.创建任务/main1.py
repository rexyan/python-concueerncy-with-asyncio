import asyncio
from util import delay


async def main():
    """
    创建任务并将它们调度到事件循环中运行，这意味着我们可以同时执行多个任务。
    当这些任务包含长时间运行的操作时，它们所等待的任何内容都将发生并行。
    :return:
    """
    sleep_for_three = asyncio.create_task(delay(3))
    print("立马输出，不阻塞")
    result = await sleep_for_three
    print(f"最终结果: {result}")


asyncio.run(main())
"""
立马输出，不阻塞
sleeping for 3 second(s)
finished sleeping for 3 second(s)
最终结果: 3
"""
