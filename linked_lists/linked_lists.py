import node


class linked_lists:
    def __init__(self):
        self.head = None
        self.tail = None


    def add_to_head(self, data):
        new_node = Node(data)
        self.head =  new_node
        self.tail = new_node

