### Porównanie drzew - time to create a tree based on the first *n* numbers of the input list

#import bibliotek

import random
import time
import gc
import matplotlib.pyplot as plt



from BSL_tree import BSLTree
from AVL_tree import AVLTree


values = [random.randint(1, 30001) for _ in range(10000)]
n = [1000,2000,3000,4000,5000,6000,7000,8000,9000,10000]

tree_avl_times =[]
tree_bsl_times =[]

for size in n:
    tree_avl = AVLTree("")
    
    gc_old = gc.isenabled()
    gc.disable()
    start = time.process_time()
    
    for val in values[:size]:
        tree_avl.insert(val)
    
    stop = time.process_time()
    if gc_old: gc.enable()

    tree_avl_times.append(stop - start)

    print(f'Time of inserting elements for AVL Tree : {stop - start} s')


for size in n:
    tree_bsl = BSLTree("")

    gc_old = gc.isenabled()
    gc.disable()
    start = time.process_time()
    
    for val in values[:size]:
        tree_bsl.insert(val)
    
    stop = time.process_time()
    if gc_old: gc.enable()

    tree_bsl_times.append(stop - start)

    print(f'Time of inserting elements for BSL Tree : {stop - start} s')

plt.plot(n, tree_avl_times, marker='o', label='AVL Tree')
plt.plot(n, tree_bsl_times, marker='o', label='BSL Tree')

plt.title("Time of inserting elements")
plt.xlabel("Number of elements")
plt.ylabel("Time (s)")
plt.legend()
plt.grid(True)
plt.show()