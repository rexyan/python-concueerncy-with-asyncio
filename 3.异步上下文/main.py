import asyncio

class AsyncContextManager:
    async def __aenter__(self):
        print("进入上下文管理器")
        # 在这里可以执行一些异步操作
        await asyncio.sleep(1)
        return "进入上下文管理器成功"

    async def __aexit__(self, exc_type, exc_value, traceback):
        print("离开上下文管理器")
        # 在这里可以执行一些异步操作
        await asyncio.sleep(1)
        if exc_type is not None:
            print(f"发生异常：{exc_type}, {exc_value}, {traceback}")
        else:
            print("没有发生异常")

async def main():
    async with AsyncContextManager() as result:
        print(result)

asyncio.run(main())

