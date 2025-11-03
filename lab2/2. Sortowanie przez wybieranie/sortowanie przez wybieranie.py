# sortowanie przez wybieranie (ang. selection sort)

import os
import string
import time
import gc
import matplotlib.pyplot as plt


def selection_sort(slowa):
    slowa = slowa.copy()
    for i in range(0, len(slowa)):
        min_idx = i
        for j in range(i +1,len(slowa)):
            if slowa[j] < slowa[min_idx]:
                min_idx = j
        slowa[i], slowa[min_idx] = slowa[min_idx], slowa[i]
    return slowa

# wczytanie pliku
sciezka_skryptu = os.path.dirname(__file__)
plik = os.path.join(sciezka_skryptu, "pan-tadeusz.txt")

with open('pan-tadeusz.txt', 'r', encoding='utf-8') as f:
    zawartosc_pliku = f.read()
    slowa = zawartosc_pliku.lower().split()

#oczyszczanie tekstu przez pominiecie w sortowaniu podstawowej interpunkcji + dodatkowej
def oczysc_slowo(s):
    return s.strip(string.punctuation + "«»…")

czyste_slowa = [oczysc_slowo(s) for s in slowa if oczysc_slowo(s)]

# usuwanie duplikatów za pomocą set
unikalne_slowa = list(set(czyste_slowa))

# test na pierwszych 100 słowach
test_sortowania = selection_sort(slowa[:1000])  
if test_sortowania == sorted(slowa[:1000], key=str.lower):
    print("selection_sort: poprawnie sortuje")
else:
    print("selection_sort: BŁĄD SORTOWANIA!")


# czas sortowania i odśmiecanie

rozmiar_listy = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
czas_sortowania = []

for n in rozmiar_listy:
    lista_testowa = slowa[:n]
    gc_old = gc.isenabled()
    gc.disable() 

    start = time.process_time() 
    selection_sort(lista_testowa)
    stop = time.process_time()
    if gc_old: gc.enable() 
    czas_sortowania.append(stop - start)
    print('Czas wykonania w sekundach:', stop - start)

# wykres
plt.plot(rozmiar_listy, czas_sortowania, marker='o', linestyle='-', color='pink')
plt.title("Czas sortowania")
plt.xlabel("Liczba elementów")
plt.ylabel("Czas [s]")
plt.grid(True)
plt.savefig("wykres_sort_przez_wybieranie.png") 
