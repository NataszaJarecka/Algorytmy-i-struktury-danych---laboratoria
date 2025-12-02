# Test of deleting elements in BSL Tree

import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from BSL_tree import BSLTree

example_values = [69, 10, 992, 612, 112, 628, 240, 817, 533, 38, 784, 971]
deleting_val = example_values[1],example_values[4], example_values[6], example_values[8]

if __name__ == "__main__":
    tree_bsl= BSLTree("")

    print("BSL_tree:")
    print(" --> values to insert:", example_values)
    print(

    )
    for value in example_values:
        tree_bsl.insert(value)
tree_bsl.print_ascii_tree()

for value in deleting_val:
    tree_bsl.delete(value)
# tree_bsl.print_ascii_tree()

print("\nResults after deletions:")
for v in example_values:
    found = tree_bsl.search(v)
    print(f"  {v}: {'FOUND' if found else 'NOT FOUND'}")

tree_bsl.print_ascii_tree()
