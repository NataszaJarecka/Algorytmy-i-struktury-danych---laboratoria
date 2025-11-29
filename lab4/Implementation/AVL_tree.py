from Node import Node

class AVLTree:

    def __init__(self, data):
        self.root = None
        self.data = data
        self.build_tree()


    def build_tree(self):
        for value in self.data:
            self.insert(value)

    def height(self, node):
        if node is None:
            return 0
        return node.height

    def get_balance_factor(self, node):
        if not node:
            return 0
        return self.height(node.left) - self.height(node.right)

    def right_rotate(self, z):
        y = z.left
        t3 = y.right

        y.right = z
        z.left = t3

        z.height = 1 + max(self.height(z.left), self.height(z.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))

        return y

    def left_rotate(self, z):
        y = z.right
        t2 = y.left

        y.left = z
        z.right = t2

        z.height = 1 + max(self.height(z.left), self.height(z.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))

        return y

    def left_right_rotate(self, z):
        z.left = self.left_rotate(z.left)

        return self.right_rotate(z)

    def right_left_rotate(self, z):
        z.right = self.right_rotate(z.right)

        return self.left_rotate(z)

    def rebalance(self, node):

        balance = self.get_balance_factor(node)

        if balance > 1:
            if self.get_balance_factor(node.left) < 0:
                return self.left_right_rotate(node)
            return self.right_rotate(node)

        if balance < -1:
            if self.get_balance_factor(node.right) > 0:
                return self.right_left_rotate(node)
            return self.left_rotate(node)

        return node

    def insert(self, element):
        self.root = self._insert(self.root, element)

    def _insert(self, node, element):

        if not node:
            return Node(element)

        if element < node.value:
            node.left = self._insert(node.left, element)
        elif element > node.value:
            node.right = self._insert(node.right, element)
        else:
            return node

        node.height = 1 + max(self.height(node.left), self.height(node.right))

        return self.rebalance(node)

    def search(self, element):

        if self.root is None:
            return False
        else:
            is_in_tree = self._search(self.root, element)
            return is_in_tree

    def _search(self, node, element):

        if node.value == element:
            return True
        elif node.right is not None and element > node.value:
            return self._search(node.right, element)
        elif node.left is not None and element < node.value:
            return self._search(node.left, element)
        else:
            return False


    def print_ascii_tree(self):
        self._print_ascii_tree(self.root)

    def _print_ascii_tree(self, node, indent="", is_last=True):
        if node is None:
            return

        if node.right:
            new_indent = indent + ("│   " if not is_last else "    ")
            self._print_ascii_tree(node.right, new_indent, False)

        connector = "└── " if is_last else "┌── "
        print(indent + connector + str(node.value))

        if node.left:
            new_indent = indent + ("    " if is_last else "│   ")
            self._print_ascii_tree(node.left, new_indent, True)


