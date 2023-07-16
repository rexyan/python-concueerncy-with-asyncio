import requests
import asyncio
from util import async_timed


def get_status_code(url: str) -> int:
    response = requests.get(url)
    return response.status_code


@async_timed()
async def main():
    urls = ['https://www.baidu.com' for _ in range(1000)]
    # 使用 to_thread 协程可以消除使用 functools.partial 和 asyncio.get_running_loop 的调用
    tasks = [asyncio.to_thread(get_status_code, url) for url in urls]
    results = await asyncio.gather(*tasks)
    print(results)


asyncio.run(main())
