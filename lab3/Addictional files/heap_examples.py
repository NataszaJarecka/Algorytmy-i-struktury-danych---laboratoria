import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from heaps import Heap2, Heap5, Heap7


example_values = [20, 15, 10, 5, 12, 7]
example_values1= [55, 74, 66, 18, 28, 85, 56, 34, 64, 83, 25, 79, 80, 63, 84, 70, 69, 2, 23, 77, 89]
example_values2= [11, 59, 45, 15, 8, 67, 100, 53, 97, 16, 50, 87, 61, 33, 30, 37, 69, 2, 23, 77, 89, 86, 29]

if __name__ == "__main__":
    heap2 = Heap2()
    print("2-ary heap:")
    for val in example_values:
        heap2.push(val)
        print("2-ary heap: next element", val)
        heap2.print_ascii_tree()


    heap5 = Heap5()
    print("5-ary heap:")
    for val in example_values1:
        heap5.push(val)
        print("5-ary heap: next element", val)
        heap5.print_ascii_tree()


    heap7 = Heap7()
    print("7-ary heap:")
    for val in example_values2:
        heap7.push(val)
        print("7-ary heap: next element", val)
        heap7.print_ascii_tree()





