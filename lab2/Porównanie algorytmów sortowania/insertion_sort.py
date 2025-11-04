import string

def insertion_sort(words):
    words = words.copy()
    for i in range(1, len(words)):
        key = words[i]
        j = i - 1
        while j >= 0 and words[j] > key:
            words[j + 1] = words[j]
            j -= 1
        words[j + 1] = key
    return words
