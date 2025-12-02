# Testing the insert and search functions for trees

import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from BST_tree import BSTTree
from AVL_tree import AVLTree

example_values = [69, 10, 992, 612, 112, 628, 240, 817, 533, 38, 784, 971]
search_val = input("enter the value you are searching for: ")
search_val = int(search_val)

# Checking the insertion function for an AVL tree

if __name__ == "__main__":
    tree_avl= AVLTree("")
    print("AVL_tree:")
    print(

    )
    for val in example_values:
        tree_avl.insert(val)
    tree_avl.print_ascii_tree()

    print(

# Checking the insertion function for an BST tree-----------------

    )
    tree_BST= BSTTree("")
    print("BST_tree:")
    print(

    )
    for val in example_values:
        tree_BST.insert(val)
    tree_BST.print_ascii_tree()
    print(

    )

## Checking the search function for the AVL tree----------------

    print("AVL_tree:")
    print(" --> values in tree:", example_values)
    print(" --> search value is:", search_val)
    print(
        )
    found = tree_avl.search(search_val)
    if found:
        print("value is in AVL Tree")
    else:
        print("value is not in AVL Tree")
    tree_avl.search(search_val)

    print(

    )

## Checking the search function for the BST tree----------------
    print("BST_tree:")
    print(" --> values in tree:", example_values)
    print(" --> search value is:", search_val)
    print(
    )
    found = tree_BST.search(search_val)
    if found:
        print("value is in BST Tree")
    else:
        print("value is not in BST Tree")
        tree_avl.search(search_val)


