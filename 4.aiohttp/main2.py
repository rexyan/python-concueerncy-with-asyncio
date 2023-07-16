import asyncio
import aiohttp
from aiohttp import ClientSession


async def fetch_status(session: ClientSession, url: str) -> int:
    # 覆盖main中的设置，设置总超时时间为10毫秒
    ten_millis = aiohttp.ClientTimeout(total=.01)
    async with session.get(url, timeout=ten_millis) as result:
        return result.status


async def main():
    # 总超时时间为1秒，100毫秒的连接超时时间
    session_timeout = aiohttp.ClientTimeout(total=1, connect=.1)
    async with aiohttp.ClientSession(timeout=session_timeout) as session:
        await fetch_status(session, 'https://baidu.com')


asyncio.run(main())
