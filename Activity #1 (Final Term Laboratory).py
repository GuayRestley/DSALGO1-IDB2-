from LinkedStack import LinkedStack as Stack
from PositionalList import PositionalList as PositionalList  # This import is used in the implementation

# Initialize stack and positional list
S = Stack()
P = PositionalList()

def precedence(op):
    '''Return the precedence of the given operator.'''
    if op in ('+', '-'):
        return 1
    if op in ('*', '/'):
        return 2
    return 0

def infix_to_postfix(expression):
    '''Convert infix expression to postfix expression.'''
    output = []
    tokens = expression.replace('(', ' ( ').replace(')', ' ) ').split()  # Split by spaces and handle parentheses

    for token in tokens:
        if token.isnumeric() or token.isidentifier():  # If the token is an operand (number or variable)
            output.append(token)
        elif token == '(':
            S.push(token)
        elif token == ')':
            while not S.is_empty() and S.top() != '(':
                output.append(S.pop())
            if not S.is_empty():  # Ensure there is a '(' to pop
                S.pop()  # Pop the '(' from the stack
        else:  # The token is an operator
            while (not S.is_empty() and precedence(S.top()) >= precedence(token)):
                output.append(S.pop())
            S.push(token)

    # Pop all the operators from the stack
    while not S.is_empty():
        output.append(S.pop())

    return ' '.join(output)

# Get user input for the expression
expression = input("Enter an infix expression: ")
postfix_expression = infix_to_postfix(expression)
print("Postfix Expression:", postfix_expression)
from LinkedStack import LinkedStack as Stack
from PositionalList import PositionalList as PositionalList

S = Stack()

P = PositionalList()
P.add_first(1)
P.add_first(72)
P.add_first(81)
P.add_first(25)
P.add_first(65)
P.add_first(91)
P.add_first(11)

print("Displaying the current values in Positional List P")
for x in P:
    print(x)

def insertion_sort(L):
    if len(L) > 1:
        marker = L.first()
        while marker != L.last():
            pivot = L.after(marker)
            value = pivot.element()
            if value > marker.element():
                marker = pivot
            else:
                walk = marker
                while walk != L.first() and L.before(walk).element() > value:
                    walk = L.before(walk)
                L.delete(pivot)
                L.add_before(walk, value)
insertion_sort(P)
print("The sorted list of elements in Ascending Order are: ")
for x in P:
    print(x)

def insertion_sort(L):
    if len(L) > 1:
        marker = L.first()
        while marker != L.last():
            pivot = L.after(marker)
            value = pivot.element()
            if value < marker.element():
                marker = pivot
            else:
                walk = marker
                while walk != L.first() and L.before(walk).element() < value:
                    walk = L.before(walk)
                L.delete(pivot)
                L.add_before(walk, value)
insertion_sort(P)
print("The sorted list of elements in Descending Order are: ")
for x in P:
    print(x)
