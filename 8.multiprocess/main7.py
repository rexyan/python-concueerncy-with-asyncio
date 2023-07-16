from multiprocessing import Process, Value


def increment_value(shared_int: Value):
    # 获取锁
    shared_int.get_lock().acquire()
    shared_int.value = shared_int.value + 1
    # 释放锁
    shared_int.get_lock().release()


if __name__ == '__main__':
    for _ in range(100):
        # 需要注意这里的待加锁对象需要使用 multiprocessing 模块中的 Value 进行包装
        integer = Value('i', 0)
        procs = [
            Process(target=increment_value, args=(integer,)),
            Process(target=increment_value, args=(integer,))
        ]

        [p.start() for p in procs]
        [p.join() for p in procs]
        print(integer.value)
        assert (integer.value == 2)
