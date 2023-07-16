import asyncio
import functools

import requests

from util import async_timed


def get_status_code(url: str) -> int:
    response = requests.get(url)
    return response.status_code


@async_timed()
async def main():
    loop = asyncio.get_running_loop()
    urls = ['https://www.baidu.com' for _ in range(1000)]
    # 使用默认值执行器 ThreadPoolExecutor
    tasks = [loop.run_in_executor(None, functools.partial(get_status_code, url)) for url in urls]
    results = await asyncio.gather(*tasks)
    print(results)


asyncio.run(main())
