class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
        print(f"Stack after push({item}): {self.items}")

    def pop(self):
        if self.is_empty():
            return "Error: Stack is empty"
        item = self.items.pop()
        print(f"Popped item: {item}, Stack now: {self.items}")
        return item

    def top(self):
        if self.is_empty():
            return "Error: Stack is empty"
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def __len__(self):
        return len(self.items)


# First set of operations
S = Stack()
operations = [
    ("S.push(5)",),
    ("S.push(3)",),
    ("len(S)",),
    ("S.pop()",),
    ("S.is_empty()",),
    ("S.pop()",),
    ("S.is_empty()",),
    ("S.pop()",),
    ("S.push(7)",),
    ("S.push(9)",),
    ("S.top()",),
    ("S.push(4)",),
    ("len(S)",),
    ("S.pop()",),
    ("S.push(6)",),
    ("S.push(8)",),
    ("S.pop()",)
]

# Execute the first set of operations
for operation in operations:
    op = operation[0]
    if op.startswith("S.push"):
        item = int(op[7:-1])
        S.push(item)
    elif op == "len(S)":
        print(f"Length of stack: {len(S)}")
    elif op == "S.pop()":
        S.pop()
    elif op == "S.is_empty()":
        print(f"Is stack empty? {S.is_empty()}")
    elif op == "S.top()":
        print(f"Top element: {S.top()}")

print()  # Print a blank line for spacing

# Second set of operations
stack = Stack()
operations2 = [
    ("push(5)",),
    ("push(3)",),
    ("pop()",),
    ("push(2)",),
    ("push(8)",),
    ("pop()",),
    ("pop()",),
    ("push(9)",),
    ("push(1)",),
    ("pop()",),
    ("push(7)",),
    ("push(6)",),
    ("pop()",),
    ("pop()",),
    ("push(4)",),
    ("pop()",),
    ("pop()",)
]

# Execute the second set of operations
returned_values = []
for operation in operations2:
    op = operation[0]
    if op.startswith("push"):
        item = int(op[5:-1])
        stack.push(item)
    elif op == "pop()":
        returned_values.append(stack.pop())

# Final returned values
print("\nReturned values from pop operations:", returned_values)
