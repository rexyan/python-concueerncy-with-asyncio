import asyncio
import logging

import aiohttp

from util import async_timed, fetch_status


@async_timed()
async def main():
    async with aiohttp.ClientSession() as session:
        fetchers = [
            asyncio.create_task(fetch_status(session, 'python://bad.com')),
            asyncio.create_task(fetch_status(session, 'https://www.baidu.com', delay=3)),
            asyncio.create_task(fetch_status(session, 'https://www.baidu.com', delay=3))
        ]

        done, pending = await asyncio.wait(fetchers, return_when=asyncio.FIRST_EXCEPTION)

        print(f'已完成的任务数量: {len(done)}')
        print(f'阻塞的任务数量: {len(pending)}')
        for done_task in done:
            if done_task.exception() is None:
                print(done_task.result())
            else:
                logging.error("请求异常", exc_info=done_task.exception())

        # 取消正在运行的请求
        for pending_task in pending:
            print(f"取消任务: {pending_task}")
            pending_task.cancel()


asyncio.run(main())
