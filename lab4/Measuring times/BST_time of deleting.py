#Time for deleting elements from BSL Tree

import random
import time
import gc
import matplotlib.pyplot as plt



from BSL_tree import BSLTree


values = [random.randint(1, 30001) for _ in range(10000)]
n = [1000,2000,3000,4000,5000,6000,7000,8000,9000,10000]

tree_bsl_times =[]


for size in n:
    tree_bsl = BSLTree("")
    for val in values[:size]:
        tree_bsl.insert(val)

    gc_old = gc.isenabled()
    gc.disable()
    start = time.process_time()
    
    for val in values[:size]:
        tree_bsl.delete(val)
    
    stop = time.process_time()
    if gc_old: gc.enable()

    tree_bsl_times.append(stop - start)

    print(f'Time of deleting elements for BSL Tree : {stop - start} s')

plt.plot(n, tree_bsl_times, marker='o', label='BSL Tree')

plt.title("Time of deleting elements from BSL Tree")
plt.xlabel("Number of elements")
plt.ylabel("Time (s)")
plt.legend()
plt.grid(True)
plt.show()