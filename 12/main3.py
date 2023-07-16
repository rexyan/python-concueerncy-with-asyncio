class CustomFuture:

    def __init__(self):
        self._result = None
        self._is_finished = False
        self._done_callback = None

    def result(self):
        return self._result

    def is_finished(self):
        return self._is_finished

    def set_result(self, result):
        self._result = result
        self._is_finished = True
        if self._done_callback:
            self._done_callback(result)

    def add_done_callback(self, fn):
        self._done_callback = fn

    def __await__(self):
        if not self._is_finished:
            yield self
        return self.result()


future = CustomFuture()
i = 0
while True:
    try:
        print('检查 future...')
        gen = future.__await__()
        gen.send(None)
        print('Future 没有完成...')
        if i == 2:
            print('设置 future 值...')
            future.set_result('Future 完成!')
        i = i + 1
    except StopIteration as si:
        print(f'迭代结束，值为: {si.value}')
        break
