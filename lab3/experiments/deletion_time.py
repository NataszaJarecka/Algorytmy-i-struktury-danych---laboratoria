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

    for val in values:
        heap2.push(val)

    gc_old = gc.isenabled()  # pobierz aktualny stan odśmiecania
    gc.disable()
    start = time.process_time()

    for _ in range(n):
        heap2.delete()

    stop = time.process_time()
    if gc_old: gc.enable()

    heap2_times.append(stop - start)

    print(f'Time of deleting {n} elements from 2-ary heap : {stop - start} s')



for n in k:
    heap5 = Heap5()

    for val in values:
        heap5.push(val)

    gc_old = gc.isenabled()  # pobierz aktualny stan odśmiecania
    gc.disable()
    start = time.process_time()

    for _ in range(n):
        heap5.delete()

    stop = time.process_time()
    if gc_old: gc.enable()

    heap5_times.append(stop - start)

    print(f'Time of deleting {n} elements from 5-ary heap : {stop - start} s')



for n in k:
    heap7 = Heap7()

    for val in values:
        heap7.push(val)

    gc_old = gc.isenabled()  # pobierz aktualny stan odśmiecania
    gc.disable()
    start = time.process_time()

    for _ in range(n):
        heap7.delete()

    stop = time.process_time()
    if gc_old: gc.enable()

    heap7_times.append(stop - start)

    print(f'Time of deleting {n} elements from 7-ary heap : {stop - start} s')



plt.plot(k, heap2_times, marker='o', label='2-ary heap')
plt.plot(k, heap5_times, marker='s', label='5-ary heap')
plt.plot(k, heap7_times, marker='^', label='7-ary heap')

plt.title("Time of deleting elements from heaps")
plt.xlabel("Number of elements")
plt.ylabel("Time (s)")
plt.legend()
plt.grid(True)
plt.show()