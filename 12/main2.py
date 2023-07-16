import asyncio
from asyncio import StreamReader, StreamWriter
import uvloop


async def connected(reader: StreamReader, writer: StreamWriter):
    line = await reader.readline()
    writer.write(line)
    await writer.drain()
    writer.close()
    await writer.wait_closed()


async def main():
    server = await asyncio.start_server(connected, port=9000)
    await server.serve_forever()

# 切换事件循环
uvloop.install()
asyncio.run(main())

# 或者采用这种方式切换
"""
loop = uvloop.new_event_loop()
asyncio.set_event_loop(loop)
"""