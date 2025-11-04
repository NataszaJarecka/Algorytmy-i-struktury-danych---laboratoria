import time
import gc
import matplotlib.pyplot as plt
import string


from bubble_sort import bubble_sort
from insertion_sort import insertion_sort
from merge_sort import merge_sort
from quick_sort import quick_sort
from selection_sort import selection_sort

def clean_word(s):
    return s.strip(string.punctuation + "«»…").lower()

with open("pan-tadeusz.txt", "r", encoding="utf-8") as f:
    words = [clean_word(w) for w in f.read().split() if clean_word(w)]

list_size = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
algorithms = {
    "Bubble": bubble_sort,
    "Insertion": insertion_sort,
    "Merge": merge_sort,
    "Quick": quick_sort,
    "Selection": selection_sort
}

results = {}
for name, func in algorithms.items():
    times = []
    print(f"\n{name} sort:")
    for n in list_size:
        test = words[:n].copy()
        gc.disable()
        start = time.perf_counter()
        func(test)
        stop = time.perf_counter()
        gc.enable()
        elapsed = stop - start
        times.append(elapsed)
        print(f"  n={n}: {elapsed:.4f}s")
    results[name] = times

for name, times in results.items():
    plt.plot(list_size, times, marker='o', label=name)

plt.title("Porównanie algorytmów sortowania")
plt.xlabel("Liczba elementów")
plt.ylabel("Czas [s]")
plt.grid(True)
plt.legend(title="Algorytmy") 
plt.savefig("sort.png")
