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

    def is_sorted(self):
        if self.head is None or self.head.data == self.tail.data:
            return True

        cur_node = self.head
        while cur_node.next:
            if cur_node > cur_node.next:
                return False
            cur_node.data = cur_node.next.data

        return True

    def get_size(self):
        cur_node = self.head
        count = 0
        while cur_node:
            count += 1
            cur_node = cur_node.next

        return count

    def get_max(self):
        if self.head is None:
            return False

        max_node = self.head
        cur_node = self.head
        while cur_node.next:
            if cur_node.data > max_node.data:
                max_node = cur_node
            cur_node = cur_node.next

        return max_node

    def get_min(self):
        if self.head is None:
            print("List is empty!")
            return

        min_node = self.head
        cur_node = self.head
        while cur_node.next:
            if cur_node.data < min_node.data:
                min_node = cur_node
            cur_node = cur_node.next

        return min_node

    def append_list(self, linked_list):
        if linked_list.head is None:
            return

        cur_node = linked_list.head()
        while cur_node:
            self.add_to_tail(cur_node.data)
            cur_node = cur_node.next

    def reversed(self):
        if self.head is None:
            return None

        cur_node = self.head
        new_list = linked_lists()
        while cur_node:
            new_list.add_to_head(cur_node.data)
            cur_node = cur_node.next

        return new_list

    def reverse_list(self):

        tmp_list = linked_lists()

        while self.head is not None:
            tmp_list.add_to_head(self.head.data)
            self.remove_head

        self.append_list(tmp_list)

    def reverse(self):

        cur_node = self.head
        prev_node = None
        while cur_node:
            next_node = cur_node.next
            cur_node.next = prev_node
            prev_node = cur_node
            cur_node = next_node

    def summation(self, k):
        if self.head is None:
            return None

        cur_node = self.head
        total = 0
        while k > 0:
            if not cur_node:
                raise IndexError
            total += cur_node.data
            cur_node = cur_node.next
            k -= 1

        return total

    def remove_duplicates(self):
        if self.head is None:
            return None
        cur_node = self.head
        while cur_node.next:
            if cur_node.data == cur_node.next.data:
                cur_node.next = cur_node.next.next
                continue
            cur_node = cur_node.next

    def display(self):
        cur_node = self.head
        while cur_node.next:
            print(cur_node.data, end=" ---> ")
            cur_node = cur_node.next
        print("None")


# Test
linked_list = linked_lists()

for i in range(10):
    linked_list.add_to_tail(i)

linked_list.insert_at_index(200, 5)
linked_list.insert_at_index(200, 5)
linked_list.insert_at_index(200, 5)
linked_list.insert_at_index(200, 5)

linked_list.display()
linked_list.remove_duplicates()
linked_list.display()
