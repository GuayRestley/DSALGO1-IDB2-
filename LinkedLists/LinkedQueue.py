class LinkedQueue:
    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Exception('Queue is empty')
        return self._head._element

    def dequeue(self):
        if self.is_empty():
            raise Exception('Queue is empty')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return answer

    def enqueue(self, e):
        newest = self._Node(e, None)
        if self.is_empty():
            self._head = newest
        else:
            self._tail._next = newest
        self._tail = newest
        self._size += 1

    def rotate(self):
        if self._size > 0:
            old_head = self._head
            self._head = old_head._next
            self._tail._next = old_head
            old_head._next = None
            self._tail = old_head


D = [1, 2, 3, 4, 5, 6, 7, 8]
print("Initial deque D =", D)

Q = LinkedQueue()

for _ in range(3):
    Q.enqueue(D.pop(0))

Q.enqueue(D.pop(0))

Q.enqueue(D.pop(0))

while D:
    Q.enqueue(D.pop(0))

D.append(Q.dequeue())
D.append(Q.dequeue())
D.append(Q.dequeue())
Q.rotate()

D.append(Q.dequeue())
Q.rotate()
D.append(Q.dequeue())
D.append(Q.dequeue())
D.append(Q.dequeue())

print("Final deque D =", D)
