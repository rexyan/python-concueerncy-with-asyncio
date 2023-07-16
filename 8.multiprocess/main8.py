import asyncio
from concurrent.futures import ProcessPoolExecutor
from multiprocessing import Value

shared_counter: Value


def init(counter: Value):
    # 声明为全局变量，并且将值设置为 multiprocessing 中的 Value 类型
    global shared_counter
    shared_counter = counter


def increment():
    # 从全局变量去获取锁
    with shared_counter.get_lock():
        shared_counter.value += 1


async def main():
    counter = Value('d', 0)
    # 进程池执行器支持传入初始化函数和初始化函数的参数
    with ProcessPoolExecutor(initializer=init, initargs=(counter,)) as pool:
        await asyncio.get_running_loop().run_in_executor(pool, increment)
        print(counter.value)


if __name__ == "__main__":
    asyncio.run(main())
