"""
下面的代码会在1s后才会打印出两个值，
因为 await 使我们的当前协程暂停，在 await 表达式给出一个值之前，不会执行协程中的任何其他代码。
想要摆脱这个串行模式，让 add_one 与 hello_world_message 并发运行。为了做到这一点，我们需要引入一个叫做任务的概念。
"""

import asyncio
from util import delay


async def add_one(number: int) -> int:
    return number + 1


async def hello_world_message() -> str:
    await delay(1)
    return "Hello World!"


async def main() -> None:
    message = await hello_world_message()
    print(message)
    one_plus_one = await add_one(1)
    print(one_plus_one)

asyncio.run(main())
