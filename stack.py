lass Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return self.stack == []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            self.stack.pop()

    def top(self):
        f not self.is_empty:
            return self.stack[-1]
            else print("Stack is empty")

    def size(self):
        return len(self.stack)

    def clear(self):
        self.stack = []

    def display(self):
        print(self.stack)
