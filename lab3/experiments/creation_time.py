import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from heaps import Heap2, Heap5, Heap7

import random

import time
import gc

import matplotlib.pyplot as plt

values = [random.randint(1, 300000) for _ in range(100000)]
k = [10000, 20000, 50000, 80000, 100000]

heap2_times = []
heap5_times = []
heap7_times = []

for n in k:
    heap2 = Heap2()

    gc_old = gc.isenabled()  # pobierz aktualny stan odśmiecania
    gc.disable()
    start = time.process_time()

    for val in values[:n]:
        heap2.push(val)

    stop = time.process_time()
    if gc_old: gc.enable()

    heap2_times.append(stop - start)

    print(f'Time of creating a 2-ary heap with {n} elements : {stop - start} s')



for n in k:
    heap5 = Heap5()

    gc_old = gc.isenabled()  # pobierz aktualny stan odśmiecania
    gc.disable()
    start = time.process_time()

    for val in values[:n]:
        heap5.push(val)

    stop = time.process_time()
    if gc_old: gc.enable()

    heap5_times.append(stop - start)

    print(f'Time of creating a 5-ary heap with {n} elements : {stop - start} s')


for n in k:
    heap7 = Heap7()

    gc_old = gc.isenabled()  # pobierz aktualny stan odśmiecania
    gc.disable()
    start = time.process_time()

    for val in values[:n]:
        heap7.push(val)

    stop = time.process_time()
    if gc_old: gc.enable()

    heap7_times.append(stop - start)

    print(f'Time of creating a 7-ary heap with {n} elements : {stop - start} s')


plt.plot(k, heap2_times, marker='o', label='2-ary heap')
plt.plot(k, heap5_times, marker='s', label='5-ary heap')
plt.plot(k, heap7_times, marker='^', label='7-ary heap')

plt.title("Time of creating heaps")
plt.xlabel("Number of elements")
plt.ylabel("Time (s)")
plt.legend()
plt.grid(True)
plt.show()