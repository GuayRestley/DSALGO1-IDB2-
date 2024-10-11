class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)
        print(f"Enqueued: {item}, Queue: {self.items}")

    def dequeue(self):
        if not self.is_empty():
            item = self.items.pop(0)
            print(f"Dequeued: {item}, Queue: {self.items}")
            return item
        else:
            raise IndexError("Dequeue from empty queue")

    def is_empty(self):
        return len(self.items) == 0

    def first(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("Queue is empty")

    def __len__(self):
        return len(self.items)

    def __repr__(self):
        return repr(self.items)

Q = Queue()

Q.enqueue(5)
Q.enqueue(3)
print(f"Length of queue: {len(Q)}")
Q.dequeue()
print(f"Is empty: {Q.is_empty()}")
Q.dequeue()
print(f"Is empty: {Q.is_empty()}")
try:
    Q.dequeue()
except IndexError as e:
    print(e)

Q.enqueue(7)
Q.enqueue(9)
try:
    print(f"First item: {Q.first()}")
except IndexError as e:
    print(e)

Q.enqueue(4)
print(f"Length of queue: {len(Q)}")
Q.dequeue()

print(f"Final Queue: {Q}")





#part 2
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)
        print(f"Enqueued: {item}, Queue: {self.items}")

    def dequeue(self):
        if not self.is_empty():
            item = self.items.pop(0)
            print(f"Dequeued: {item}, Queue: {self.items}")
            return item
        else:
            raise IndexError("Dequeue from empty queue")

    def is_empty(self):
        return len(self.items) == 0

    def first(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("Queue is empty")

    def __len__(self):
        return len(self.items)

    def __repr__(self):
        return repr(self.items)

Q = Queue()


Q.enqueue(5)
Q.enqueue(3)
Q.dequeue()
Q.enqueue(2)
Q.enqueue(8)
Q.dequeue()
Q.dequeue()
Q.enqueue(9)
Q.enqueue(1)
Q.dequeue()
Q.enqueue(7)
Q.enqueue(6)
Q.dequeue()
Q.dequeue()
Q.enqueue(4)
Q.dequeue()
Q.dequeue()

