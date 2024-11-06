

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None


class dll:
    def __init__(self):
        self.tail = None
        self.head = None

    def is_empty(self):
        return self.head is None

    def get_head(self):
        return self.head

    def get_head_data(self):
        return self.head.data

    def get_tail(self):
        return self.tail

    def get_tail_data(self):
        return self.tail.data

    def is_in_list(self, data):
        cur = self.head
        while cur:
            if cur.data == data:
                return True
            cur = cur.next

        return False

    def add_to_head(self, data):
        new = Node(data)
        if self.is_empty():
            self.head = new
            self.tail = new
            return

        self.head.prev = new
        new.next = self.head
        self.head = new.next

    def add_to_tail(self, data):
        new = Node(data)
        if self.is_empty():
            self.head = new
            self.tail = new

        self.tail.next = new
        new.prev = self.tail
        self.tail = new

    def display(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data, end=" ---> ")
            cur_node = cur_node.next
        print("None")

    def display_reverse(self):
        cur = self.tail
        while cur:
            print(cur.data, end="-->")
            cur = cur.prev

        print("None")

    def remove_from_head(self):
        if self.is_empty():
            return
        if self.tail == self.head:
            self.tail = None
            self.head = None

        self.head = self.head.next
        self.head.prev = None

    def remove_from_tail(self):
        if self.is_empty():
            return
        if self.tail == self.head:
            self.tail = None
            self.head = None

        self.tail = self.tail.prev
        self.tail.next = None

    def remove_data(self, data):
        if self.is_empty():
            return

        if self.head.data == data:
            self.remove_from_head()
            return

        if self.tail.data == data:
            self.remove_from_tail()
            return

        cur = self.head
        while cur:
            if cur.data == data:
                cur.prev.next = cur.next
                cur.next.prev = cur.prev
                return
            cur = cur.next

        return False

    def remove_all_data(self, data):
        if self.is_empty():
            return

        cur = self.head
        while cur:
            if cur.data == data:
                if cur == self.head:
                    self.remove_from_head()
                elif cur == self.tail:
                    self.remove_from_tail()
                else:
                    cur.prev.next = cur.next
                    cur.next.prev = cur.prev
            cur = cur.next


# Test

ll = dll()

ll.add_to_head(1)
ll.add_to_head(1)
ll.add_to_head(3)
ll.add_to_head(2)
ll.add_to_head(2)

ll.display()

ll.remove_all_data(2)

ll.display()
