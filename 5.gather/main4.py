import asyncio

import aiohttp

from util import async_timed, fetch_status


@async_timed()
async def main():
    async with aiohttp.ClientSession() as session:
        urls = ['https://baidu.com', 'python://example.com']
        tasks = [fetch_status(session, url) for url in urls]
        results = await asyncio.gather(*tasks, return_exceptions=True)

        # 遍历所有的结果，获取异常的结果
        exceptions = [res for res in results if isinstance(res, Exception)]
        # 遍历所有的结果，获取正常的结果
        successful_results = [res for res in results if not isinstance(res, Exception)]

        print(f'All results: {results}')
        print(f'Finished successfully: {successful_results}')
        print(f'Threw exceptions: {exceptions}')

asyncio.run(main())