class LinkedStack:
    '''LIFO Stack implementation using a singly linked list for storage.'''

    class _Node:
        '''Lightweight non-public class for storing a singly linked node.'''
        __slots__ = '_element', '_next'  # streamline memory usage

        def __init__(self, element, next):
            self._element = element
            self._next = next

    # Stack Methods
    def __init__(self):
        '''Create an empty Stack'''
        self._head = None
        self._size = 0

    def __len__(self):
        '''Return the number of elements in the stack'''
        return self._size

    def is_empty(self):
        '''Return True if the stack is empty.'''
        return self._size == 0

    def push(self, e):
        '''Add element e to the top of the stack.'''
        self._head = self._Node(e, self._head)
        self._size += 1

    def top(self):
        '''Return but do not remove the element at the top of the stack'''
        if self.is_empty():
            raise Exception('Stack is empty')
        return self._head._element

    def pop(self):
        '''Remove and return the elements from the top of the stack (LIFO)'''
        if self.is_empty():
            raise Exception("The stack is empty!")
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        return answer


def insertion_sort_linked_stack(stack, ascending=True):
    '''Sort a linked stack using the insertion sort algorithm.'''
    sorted_stack = LinkedStack()

    while not stack.is_empty():
        current_element = stack.pop()

        while not sorted_stack.is_empty() and (
            (ascending and sorted_stack.top() > current_element) or
            (not ascending and sorted_stack.top() < current_element)):
            stack.push(sorted_stack.pop())

        sorted_stack.push(current_element)

    while not sorted_stack.is_empty():
        stack.push(sorted_stack.pop())


def print_stack(stack):
    '''Print the elements of the stack from top to bottom.'''
    elements = []
    while not stack.is_empty():
        elements.append(stack.pop())
    for elem in reversed(elements):
        print(elem, end=" ")
    print()

def main():
    numbers = input("Enter a number: ")

    stack = LinkedStack()
    for num in numbers:
        stack.push(num)

    insertion_sort_linked_stack(stack, ascending=True)
    print("Sorted in Ascending Order:")
    print_stack(stack)

    for num in numbers:
        stack.push(num)

    insertion_sort_linked_stack(stack, ascending=False)
    print("Sorted in Descending Order:")
    print_stack(stack)


if __name__ == "__main__":
    main()
