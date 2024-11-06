from Node import Node


class OrderedDLL:
    def __init__(self):
        self.tail = None
        self.head = None

    def is_empty(self):
        if self.head is None:
            return True

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

    def add_node(self, data):
        nn = Node(data)
        if self.is_empty():
            self.head = nn
            self.tail = nn
            return

        if nn.data < self.head.data:
            nn.next = self.head
            self.head.prev = nn
            self.head = nn
            return

        if nn.data > self.tail.data:
            self.tail.next == nn
            nn.prev = self.tail
            self.tail = nn
            return

        cur = self.head
        while cur:
            if cur.data <= nn.data:
                cur = cur.next
            else:
                cur.prev.next = nn
                nn.prev = cur.prev
                cur.prev = nn
                nn.next = cur

    def merge_in_order(self, ll):
        if ll.head is None:
            return

        if self.head is None:
            self.head = ll.head
            self.tail = ll.tail
            return

        ll_cur = ll.head
        cur = self.head
        last_sorted = None

        while ll_cur and ll_cur.data <= cur.data:
            last_sorted = ll_cur
            ll_cur = ll_cur.next
            self.head.prev == last_sorted
            last_sorted.next = self.head
            self.head = last_sorted

        while cur and ll_cur:
            if cur.data < ll_cur.data:
                last_sorted = cur
                cur = cur.next
            else:
                last_sorted = ll_cur
                ll_cur = ll_cur.next
                last_sorted.prev = cur.prev
                cur.prev.next = last_sorted
                cur.prev = last_sorted
                last_sorted.next = cur

        if not ll_cur:
            return
        else:
            while ll_cur:
                ll_cur.prev = last_sorted
                last_sorted.next = ll_cur
                last_sorted = ll_cur
                self.tail = last_sorted
                ll_cur.prev = last_sorted

    def display(self):
        cur = self.head
        while cur:
            print(cur.data, end=" ---> ")
            cur = cur.next
        print("None")

    def display_reverse(self):
        cur = self.tail
        while cur:
            print(cur.data, end=" ---> ")
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

ll = OrderedDLL()

ll.add_node(3)
ll.add_node(4)
ll.add_node(5)
ll.add_node(6)

ll.display()

ll.display_reverse()
