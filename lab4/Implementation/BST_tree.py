from Node import Node

class BSTTree:

    def __init__(self, data):
        self.root = None
        self.data = data
        self.build_tree()


    def build_tree(self):
        for value in self.data:
            self.insert(value)

    def insert(self, element):
        self.root = self._insert(self.root, element)

    def _insert(self, node, element):

        if not node:
            return Node(element)

        if element < node.value:
            node.left = self._insert(node.left, element)
        elif element > node.value:
            node.right = self._insert(node.right, element)

        return node

    def delete(self, element):
        self.root = self._delete(self.root, element)

    def _delete(self, node, element):

        if node is None:
            return None

        if element < node.value:
            node.left = self._delete(node.left, element)
        elif element > node.value:
            node.right = self._delete(node.right, element)
        else:

            if node.left is None and node.right is None:
                return None

            if node.left is None:
                return node.right
            if node.right is None:
                return node.left

            successor = self.find_min(node.right)
            node.value = successor.value
            node.right = self._delete(node.right, successor.value)

        return node


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


    def find_min(self, node):
        if node.left is None:
            return node
        return self.find_min(node.left)


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
