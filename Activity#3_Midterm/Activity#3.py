class DeQueue:
    DEFAULT_CAPACITY = 10
    def _init_(self):
        self._data = [None] * DeQueue.DEFAULT_CAPACITY
        self._size = 0