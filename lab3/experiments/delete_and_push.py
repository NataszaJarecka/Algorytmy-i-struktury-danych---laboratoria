import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from heaps import Heap2, Heap5, Heap7

import random

def check_max_heap(heap, k):
    arr = heap.Heap
    n = len(arr)

    for parent_index in range(n):
        for i in range(1, k+1):
            child_index = k * parent_index + i
            if child_index < n:
                if arr[parent_index] < arr[child_index]:
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

heap2.push(400)
heap5.push(400)
heap7.push(400)

print("Checking max-heap property after insertions:")

print(check_max_heap(heap2, 2))
print(check_max_heap(heap5, 5))
print(check_max_heap(heap7, 7))


heap2.delete()
heap5.delete()
heap7.delete()

print("Checking max-heap property after deletions:")

print(check_max_heap(heap2, 2))
print(check_max_heap(heap5, 5))
print(check_max_heap(heap7, 7))