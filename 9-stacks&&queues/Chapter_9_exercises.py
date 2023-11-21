class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Stack is empty")

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

    def size(self):
        return len(self.items)

# Create a stack
stack = Stack()

# Push elements onto the stack
stack.push(1)
stack.push(2)
stack.push(3)

# Pop elements from the stack
popped_item = stack.pop()
print(popped_item)

# Check if the stack is empty
is_empty = stack.is_empty()
print(is_empty)


def reverse_string(input_string):
    # Create a stack
    stack = Stack()

    # Push each character of the input string onto the stack
    for char in input_string:
        stack.push(char)

    # Pop characters from the stack to build the reversed string
    reversed_string = ""
    while not stack.is_empty():
        reversed_string += stack.pop()

    return reversed_string

# Test the reverse_string function
input_string = "abcde"
reversed_result = reverse_string(input_string)
print(reversed_result)
