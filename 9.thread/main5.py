import functools
import requests
import asyncio
from concurrent.futures import ThreadPoolExecutor
from threading import Lock
from util import async_timed

counter_lock = Lock()
counter: int = 0


def get_status_code(url: str) -> int:
    global counter
    response = requests.get(url)
    # 上锁
    with counter_lock:
        counter = counter + 1
    return response.status_code


async def reporter(request_count: int):
    while counter < request_count:
        print(f'Finished {counter}/{request_count} requests')
        await asyncio.sleep(.5)


@async_timed()
async def main():
    loop = asyncio.get_running_loop()
    with ThreadPoolExecutor() as pool:
        request_count = 50
        urls = ['https://www.baidu.com' for _ in range(request_count)]
        # 专门输出调用进度的 task
        reporter_task = asyncio.create_task(reporter(request_count))
        # 执行请求调用的 task
        tasks = [loop.run_in_executor(pool, functools.partial(get_status_code, url)) for url in urls]
        results = await asyncio.gather(*tasks)
        await reporter_task
        print(results)


asyncio.run(main())
