import string

def selection_sort(words):
    words = words.copy()
    for i in range(0, len(words)):
        min_idx = i
        for j in range(i +1,len(words)):
            if words[j] < words[min_idx]:
                min_idx = j
        words[i], words[min_idx] = words[min_idx], words[i]
    return words
