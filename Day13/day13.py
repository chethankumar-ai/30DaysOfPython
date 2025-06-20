# Implement a stack with push, pop, and peek
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("pop from empty stack")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        raise IndexError("peek from empty stack")

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)
    def __str__(self):
        return str(self.items)      
# Example usage     
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print("Stack after pushing 1, 2, 3:", stack)
print("Peek:", stack.peek())
print("Pop:", stack.pop())
print("Stack after popping:", stack)

