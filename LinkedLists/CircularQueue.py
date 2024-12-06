class CircularQueue:
    '''Queue implementation using circularly linked list for storage.'''

    class _Node:
        '''Lightweight non-public class for storing a singly linked node.'''
        __slots__ = '_element', '_next'  # streamline memory usage

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        '''Create an empty queue'''
        self._tail = None
        self._size = 0

    def __len__(self):
        '''Return the number of elements in the queue'''
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        '''Return but do not remove the element at the front of the queue'''
        '''Raise Empty Exception if the queue is empty'''
        if self.is_empty():
            raise Exception("The queue is empty!")
        head = self._tail._next
        return head._element

    def dequeue(self):
        '''Remove and return the first element of the queue (FIFO)'''
        '''Raise Empty exception if the queue is empty'''
        if self.is_empty():
            raise Exception("Queue is empty!")
        oldhead = self._tail._next
        if self._size == 1:  # removing the only element
            self._tail = None  # queue becomes empty
        else:
            self._tail._next = oldhead._next  # bypass the old head
        self._size -= 1
        return oldhead._element

    def enqueue(self, e):
        '''Add an element to the back of the queue'''
        newest = self._Node(e, None)  # node will be the new tail node
        if self.is_empty():
            newest._next = newest  # initialize circularly
        else:
            newest._next = self._tail._next  # new node points to head
            self._tail._next = newest  # old tail points to new node
        self._tail = newest  # new node becomes the tail
        self._size += 1

    def rotate(self):
        '''Rotate front element to the back of the queue'''
        if self._size > 0:
            self._tail = self._tail._next  # old head becomes new tail

# Define the Stack class
class Stack:
    '''Stack implementation using a simple list for storage.'''

    def __init__(self):
        '''Create an empty stack.'''
        self._stack = []

    def is_empty(self):
        '''Return True if the stack is empty, otherwise False.'''
        return len(self._stack) == 0

    def push(self, element):
        '''Push an element onto the stack.'''
        self._stack.append(element)

    def pop(self):
        '''Pop an element from the stack.'''
        if self.is_empty():
            raise Exception("Stack is empty!")
        return self._stack.pop()

    def top(self):
        '''Return the top element of the stack without removing it.'''
        if self.is_empty():
            raise Exception("Stack is empty!")
        return self._stack[-1]

    def __len__(self):
        '''Return the number of elements in the stack.'''
        return len(self._stack)


D = [1, 2, 3, 4, 5, 6, 7, 8]
print("Initial deque D =", D)
Q = CircularQueue()

for _ in range(3):
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
Q.rotate()
Q.rotate()
D.append(Q.dequeue())
D.append(Q.dequeue())
D.append(Q.dequeue())
D.append(Q.dequeue())

print("Final deque D =", D)



