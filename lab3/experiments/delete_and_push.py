import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from heaps import Heap2, Heap5, Heap7

import random

def check_max_heap(heap, k):
    elements = heap.Heap
    n = len(elements)

    for parent_index in range(n):
        for i in range(1, k+1):
            child_index = k * parent_index + i
            if child_index < n:
                if elements[parent_index] < elements[child_index]:
                    return False
    return True


values = [random.randint(1, 300000) for _ in range(100000)]

heap2 = Heap2()

for val in values:
    heap2.push(val)

heap5 = Heap5()

for val in values:
    heap5.push(val)

heap7 = Heap7()

for val in values:
    heap7.push(val)

print("Checking max-heap property after insertions:")

for i in range(10):
    n = random.randint(1, 300000)
    heap2.push(n)
    heap5.push(n)
    heap7.push(n)

    if check_max_heap(heap2, 2) == False:
        print("Error in Heap2 after pushing")
    if check_max_heap(heap5, 5) == False:
        print("Error in Heap5 after pushing")
    if check_max_heap(heap7, 7) == False:
        print("Error in Heap7 after pushing")
    if i==9:
        print("All heaps are correct after insertions.")

print("Checking max-heap property after deletions:")

for i in range(10):
    heap2.delete()
    heap5.delete()
    heap7.delete()

    if check_max_heap(heap2, 2) == False:
        print("Error in Heap2 after deleting")
    if check_max_heap(heap5, 5) == False:
        print("Error in Heap5 after deleting")
    if check_max_heap(heap7, 7) == False:
        print("Error in Heap7 after deleting")
    if i==9:
        print("All heaps are correct after deletions.")

