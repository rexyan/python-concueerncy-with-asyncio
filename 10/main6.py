import asyncio
import functools
from asyncio import Event


def trigger_event(event: Event):
    event.set()


async def do_work_on_event(event: Event):
    print('等待 event...')
    await event.wait()
    print('开始工作!')
    await asyncio.sleep(1)
    print('完成工作!')
    event.clear()


async def main():
    event = asyncio.Event()
    # 5s 后触发 trigger_event，调用 event set
    asyncio.get_running_loop().call_later(5.0, functools.partial(trigger_event, event))
    # 使用 event 来控制执行
    await asyncio.gather(do_work_on_event(event), do_work_on_event(event))


asyncio.run(main())
