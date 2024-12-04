from queue import Queue

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.depth = -1
        self.height = -1


class BTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        nn = Node(data)
        if self.root is None:
            self.root = nn
            return

        cur = self.root
        prev = None
        while cur:
            prev = cur
            if data > cur.data:
                cur = cur.right
            elif data < cur.data:
                cur = cur.left
            else:
                print("No Dupliates")
                return

        if nn.data > prev.data:
            prev.right = nn
        elif nn.data < prev.data:
            prev.left = nn

    def search(self, data):
        if self.root is None:
            return None

        cur = self.root

        while cur:
            if data == cur.data:
                print("found")
                return True
            elif cur.data > data:
                cur = cur.left
            else:
                cur = cur.right
        print("not found")
        return False

    def recsearch(self, root, data):
        if root is None:
            print("not found")
            return False
        if root.data == data:
            print("found")
            return True

        if root.data > data:
            self.recsearch(root.left, data)
        elif root.data < data:
            self.recsearch(root.right, data)

    def print_in_order(self, node):
        if node is None:
            return

        if node:
            self.print_in_order(node.left)
            print(node.data)
            self.print_in_order(node.right)

    def print_pre_order(self, node):
        if node is None:
            return

        if node:
            print(node.data)
            self.print_pre_order(node.left)
            self.print_pre_order(node.right)

    def print_post_order(self, node):
        if node is None:
            return

        if node:
            self.print_post_order(node.left)
            self.print_post_order(node.right)
            print(node.data)

    def compute_height(self, node=None):
        if node is None:
            return
        else:
            if node.left is not None:
                left_height = self.compute_height(node.left)
            else:
                left_height = -1
            if node.right is not None:
                right_height = self.compute_height(node.right)
            else:
                right_height = -1

        node.height = max(left_height, right_height) + 1
        print(node.height)
        return node.height

    def compute_depth(self, node, parent):
        if node is None:
            return
        if parent is None:
            node.depth = 0
        else:
            node.depth = parent.depth + 1

        self.compute_depth(node.left, node)
        self.compute_depth(node.right, node)

    def BFS(self):
        if self.root is None:
            return

        queue1 = Queue()
        queue1.put(self.root)

        while not queue1.empty():
            cur = queue1._get()
            print(cur.data)
            if cur.left is not None:
                queue1.put(cur.left)
            if cur.right is not None:
                queue1.put(cur.right)

    def delete_node(self, node):
        prev = None
        cur = self.root

        while cur is not None and cur.data != node.data:
            prev = cur
            if cur.data < node.data:
                cur = cur.right
            else:
                cur = cur.left

        if cur is None:
            print("Not Found!")
            return

        if cur.left is not None and cur.right is not None:
            self.delete_node_2(cur)
        else:
            self.delete_node_1(cur, prev)

    def delete_node_1(self, node, prev):
        if node == self.root:
            if node.left is None:
                self.root = node.right
            else:
                self.root = node.left
        elif node == prev.right:
            if node.right is not None:
                prev.right = node.right
            else:
                prev.right = node.left
        elif node == prev.left:
            if node.right is not None:
                prev.left = node.right
            else:
                prev.left = node.left

    def delete_node_2(self, node):
        prev = node
        rep = node.left

        while rep.right is not None:
            prev = rep
            rep = rep.right

        node.data = rep.data
        self.delete_node_1(rep, prev)



tree = BTree()

tree.insert(5)
tree.insert(7)
tree.insert(8)
tree.insert(4)
tree.insert(2)
tree.insert(3)

tree.BFS()
