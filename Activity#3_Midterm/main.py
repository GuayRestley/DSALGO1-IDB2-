from ArrayStack import ArrayStack as Stack

def is_matched(expr):
    stack = Stack()
    opening = "({["
    closing = ")}]"
    matches = {')': '(', '}': '{', ']': '['}

    for char in expr:
        if char in opening:
            stack.push(char)
        elif char in closing:
            if stack.is_empty() or stack.pop() != matches[char]:
                return False

    return stack.is_empty()

# User input for expressions
user_expression_1 = input("Enter the first expression to check: ")
if is_matched(user_expression_1):
    print("The symbols are balanced!")
else:
    print("The symbols are imbalanced!")

user_expression_2 = input("Enter the second expression to check: ")
if is_matched(user_expression_2):
    print("The symbols are balanced!")
else:
    print("The symbols are imbalanced!")


def reverse_file(filename):
    stack = Stack()

    with open(filename, 'r') as file:
        for line in file:
            stack.push(line.rstrip('\n'))

    with open(filename, 'w') as file:
        for _ in range(len(stack)):  #
            file.write(stack.pop() + '\n')

reverse_file('myfile.txt')
