from LinkedStack import LinkedStack


def insertion_sort_stack(stack, ascending=True):
    """Sort elements of the stack in ascending or descending order using insertion sort."""
    auxiliary_stack = LinkedStack()

    while not stack.is_empty():
        # Extract the top element from the stack
        temp = stack.pop()

        # Place the element in the correct position in auxiliary stack
        while (not auxiliary_stack.is_empty() and
               ((ascending and auxiliary_stack.top() > temp) or
                (not ascending and auxiliary_stack.top() < temp))):
            stack.push(auxiliary_stack.pop())

        auxiliary_stack.push(temp)

    # Move elements back to the original stack
    while not auxiliary_stack.is_empty():
        stack.push(auxiliary_stack.pop())


def print_stack(stack):
    """Print stack elements."""
    elements = []
    while not stack.is_empty():
        elements.append(stack.pop())
    # Re-push elements back to stack
    for element in reversed(elements):
        stack.push(element)
    print(elements)


if __name__ == "__main__":
    # Create a stack and add numbers
    numbers = [1, 72, 81, 25, 65, 91, 11]
    stack = LinkedStack()

    for number in numbers:
        stack.push(number)

    # Sort in ascending order
    insertion_sort_stack(stack, ascending=True)
    print("Ascending order:")
    print_stack(stack)

    # Re-push numbers to the stack
    for number in numbers:
        stack.push(number)

    # Sort in descending order
    insertion_sort_stack(stack, ascending=False)
    print("Descending order:")
    print_stack(stack)
