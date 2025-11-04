import string

def bubble_sort(words):
    words = words.copy()
    for i in range(0, (len(words) -1)):
        for j in range(0, (len(words) -1 -i)):
            if words[j] > words[j+1]:
                words[j], words[j + 1] = words[j + 1], words[j]
    return words
