import random
import string
import time
import gc
import matplotlib.pyplot as plt

def quick_sort(words):
    if len(words) <= 1:
        return words

    pivot = random.choice(words)
    less_than_pivot = [word for word in words if word.lower() < pivot.lower()]
    equal_to_pivot = [word for word in words if word.lower() == pivot.lower()]
    greater_than_pivot = [word for word in words if word.lower() > pivot.lower()]

    return quick_sort(less_than_pivot) + equal_to_pivot + quick_sort(greater_than_pivot)


# wczytanie pliku

with open('pan-tadeusz.txt', 'r', encoding='utf-8') as f:
    file_content = f.read()
    words = file_content.lower().split()

#oczyszczanie tekstu przez pominiecie w sortowaniu podstawowej interpunkcji + dodatkowej
def clean_word(s):
    return s.strip(string.punctuation + "«»…")

clean_words = [clean_word(s) for s in words if clean_word(s)]

# usuwanie duplikatów za pomocą set
unique_words = list(set(clean_words))

# test na pierwszych 100 słowach
sort_test = quick_sort(words[:1000])
if sort_test == sorted(words[:1000], key=str.lower):
    print("quick_sort: poprawnie sortuje")
else:
    print("quick_sort: BŁĄD SORTOWANIA!")


# czas sortowania i odśmiecanie

list_size = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
sort_time = []

for n in list_size:
    test_list = words[:n]
    gc_old = gc.isenabled()
    gc.disable()

    start = time.process_time()
    quick_sort(test_list)
    stop = time.process_time()
    if gc_old: gc.enable()
    sort_time.append(stop - start)
    print('Czas wykonania w sekundach:', stop - start)

#wykres
plt.plot(list_size, sort_time, marker='o', linestyle='-', color='blue')
plt.title("Czas sortowania")
plt.xlabel("Liczba elementów")
plt.ylabel("Czas [s]")
plt.grid(True)
plt.savefig("wykres_quick_sort.png")