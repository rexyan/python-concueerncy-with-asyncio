import asyncio
import logging

import aiohttp

from util import fetch_status, async_timed


@async_timed()
async def main():
    async with aiohttp.ClientSession() as session:
        good_request = fetch_status(session, 'https://baidu.com')
        bad_request = fetch_status(session, 'python://bad')

        fetchers = [
            asyncio.create_task(good_request),
            asyncio.create_task(bad_request)
        ]

        # 默认是所有任务完成才返回
        done, pending = await asyncio.wait(fetchers)

        print(f'已完成的任务数量: {len(done)}')
        print(f'阻塞的任务数量: {len(pending)}')

        for done_task in done:
            # 判断 task 是否有异常
            if done_task.exception() is None:
                # 获取 task 结果
                print(done_task.result())
            else:
                logging.error("请求异常", exc_info=done_task.exception())


asyncio.run(main())
