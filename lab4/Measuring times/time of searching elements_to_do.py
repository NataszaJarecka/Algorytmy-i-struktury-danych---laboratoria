### Time to searching elements a tree based on the first *n* numbers of the input list


import random
import time
import gc
import matplotlib.pyplot as plt

from Implementation.BST_tree import BSTTree
from Implementation.AVL_tree import AVLTree

values = [random.randint(1, 30001) for _ in range(10000)]
n = [1000,2000,3000,4000,5000,6000,7000,8000,9000,10000]

tree_avl_times =[]
tree_bsl_times =[]

for size in n:
    tree_avl = AVLTree("")

    # Najpierw budujemy drzewo wstawiając CAŁĄ listę wejściową
    for val in values:
        tree_avl.insert(val)

    gc_old = gc.isenabled()
    gc.disable()
    start = time.process_time()

    # Mierzymy czas wyszukiwania pierwszych `size` elementów
    for val in values[:size]:
        tree_avl.search(val)

    stop = time.process_time()
    if gc_old: gc.enable()

    tree_avl_times.append(stop - start)

    print(f'Time of searching elements for AVL Tree : {stop - start} s')


for size in n:
    tree_bsl = BSTTree("")
    # Również budujemy drzewo BSL na podstawie CAŁEJ listy wejściowej
    for val in values:
        tree_bsl.insert(val)

    gc_old = gc.isenabled()
    gc.disable()
    start = time.process_time()

    # Teraz mierzymy czas wyszukiwania (a nie wstawiania)
    for val in values[:size]:
        tree_bsl.search(val)

    stop = time.process_time()
    if gc_old: gc.enable()

    tree_bsl_times.append(stop - start)

    print(f'Time of searching elements for BST Tree : {stop - start} s')

plt.plot(n, tree_avl_times, marker='o', label='AVL Tree')
plt.plot(n, tree_bsl_times, marker='o', label='BST Tree')

plt.title("Time of searching elements")
plt.xlabel("Number of elements")
plt.ylabel("Time (s)")
plt.legend()
plt.grid(True)
plt.show()