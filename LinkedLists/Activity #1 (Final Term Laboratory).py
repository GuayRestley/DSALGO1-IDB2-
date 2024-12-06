from LinkedQueue import LinkedQueue
from LinkedStack import LinkedStack
from LinkedDeque import LinkedDeque


class DequeReorder:
    def __init__(self):
        self.D = LinkedDeque()
        self.Q = LinkedQueue()
        self.S = LinkedStack()

    def populate_deque(self):
        for i in range(1, 9):
            self.D.insert_last(i)

    def print_deque(self, label):
        print(f"{label}: ", end="")
        current = self.D._header._next
        while current != self.D._trailer:
            print(current._element, end=" ")
            current = current._next
        print()

    def reorder_using_queue(self):
        self.populate_deque()
        self.print_deque("Deque D before reordering using Queue Q")


        for _ in range(8):
            self.Q.enqueue(self.D.delete_first())


        self.D.insert_last(self.Q.dequeue())
        self.D.insert_last(self.Q.dequeue())
        self.D.insert_last(self.Q.dequeue())
        self.D.insert_first(self.Q.dequeue())
        self.D.insert_last(self.Q.dequeue())
        self.D.insert_last(self.D.delete_first())
        self.D.insert_last(self.Q.dequeue())
        self.D.insert_last(self.Q.dequeue())
        self.D.insert_last(self.Q.dequeue())



        self.print_deque("Deque D after reordering using Queue Q")

    def reorder_using_stack(self):
        self.print_deque("Deque D before reordering using Stack S")

        for _ in range(8):
            self.S.push(self.D.delete_last())

        self.D.insert_last(self.S.pop())
        self.D.insert_last(self.S.pop())
        self.D.insert_last(self.S.pop())
        self.D.insert_last(self.S.pop())
        self.D.insert_first(self.S.pop())
        self.D.insert_last(self.D.delete_first())
        self.D.insert_last(self.S.pop())
        self.D.insert_last(self.S.pop())
        self.D.insert_last(self.S.pop())



        self.print_deque("Deque D after reordering using Stack S")


reorder = DequeReorder()
reorder.reorder_using_queue()
print()
reorder.reorder_using_stack()