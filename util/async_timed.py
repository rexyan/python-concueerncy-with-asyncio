import functools
import time
from typing import Callable, Any


def async_timed():
    def wrapper(func: Callable) -> Callable:
        @functools.wraps(func)
        async def wrapped(*args, **kwargs) -> Any:
            print(f'开始执行函数 {func.__name__} 参数: {args} {kwargs}')
            start = time.time()
            try:
                return await func(*args, **kwargs)
            finally:
                end = time.time()
                total = end - start
                print(f'完成执行函数 {func.__name__} 花费 {total:.4f} 秒(s)')

        return wrapped

    return wrapper