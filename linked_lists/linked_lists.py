from node import Node


class linked_lists:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_head(self, data):
        new_node = Node(data)
        if self.head is None:
            self.tail = new_node
        else:
            new_node.next = self.head
        self.head = new_node

    def add_to_tail(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node

    def insert_at_index(self, data, index):
        new_node = Node(data)
        pos = 0
        cur_node = self.head
        while cur_node and index != pos+1:
            cur_node = cur_node.next
            pos += 1
        if cur_node is not None:
            new_node.next = cur_node.next
            cur_node.next = new_node
        else:
            print("Index out of range!")

    def remove_head(self):
        if self.head is None:
            None
        else:
            self.head = self.head.next
            if self.head is None:
                self.tail = None

    def remove_tail(self):
        if self.tail is None:
            None
        elif self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            cur_node = self.head
            while cur_node.next != self.tail:
                cur_node = cur_node.next
            cur_node.next = None
            self.tail = cur_node

    def remove_at_index(self, index):
        cur_node = self.head
        pos = 0
        if index == 0:
            self.remove_head()
            return
        while cur_node and index != pos:
            prev_node = cur_node
            cur_node = cur_node.next
            pos += 1
        if cur_node is not None:
            prev_node.next = cur_node.next
        else:
            print("Index out of range!")

    def remove(self, data):
        if not self.head:
            None
        elif self.head.data == data:
            self.remove_head()
        elif self.tail.data == data:
            self.remove_tail()
        elif self.head == self.tail:
            return False

        cur_node = self.head
        while cur_node != self.tail:
            if cur_node.next.data == data:
                cur_node.next = cur_node.next.next
                return True
            cur_node = cur_node.next
        return False

    def search(self, data):
        cur_node = self.head
        while cur_node:
            if cur_node.data == data:
                return True
            cur_node = cur_node.next
        return False

    def get_at_index(self, index):
        cur_node = self.head
        pos = 0
        while cur_node is not None and index != pos:
            cur_node = cur_node.next
            pos += 1

        if cur_node is not None:
            return cur_node.data
        else:
            print("Index out of range!")

    def display(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data, end=" ---> ")
            cur_node = cur_node.next
        print("None")


# Test
linked_list = linked_lists()

for i in range(10):
    linked_list.add_to_head(i)

linked_list.display()

linked_list.insert_at_index(200, 1)

linked_list.display()

print(linked_list.get_at_index(2))

linked_list.display()
