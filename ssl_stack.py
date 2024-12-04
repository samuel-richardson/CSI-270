class Node:
    def __init__(self, data):
        self.next = None
        self.data = data

class Stack:
    def __init__(self):
        self.head = None
        self.count = 0

    def is_empty(self):
        return self.head is None

    def push(self, data):
        nn = Node(data)
        nn.next = self.head
        self.head = nn
        self.count += 1

    def pop(self):
        if self.is_empty():
            raise Exception('Stack is empty')
        return_data = self.head.data
        self.head = self.head.next
        self.count -= 1
        return return_data

    def top(self):
        if self.is_empty():
            raise Exception('stack is empty')
        return self.head.data

    def size(self):
        return self.count

    def clear(self):
        self.head = None

def display(st):
        cur = st.head

        while cur:
            print(cur.data, start='---------------\n')
            cur = cur.next
stack = Stack()

stack.push(5)
stack.push(6)
stack.push(7)

display(stack)


