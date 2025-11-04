import random
import string

def quick_sort(words):
    if len(words) <= 1:
        return words

    pivot = random.choice(words)
    less_than_pivot = [word for word in words if word.lower() < pivot.lower()]
    equal_to_pivot = [word for word in words if word.lower() == pivot.lower()]
    greater_than_pivot = [word for word in words if word.lower() > pivot.lower()]

    return quick_sort(less_than_pivot) + equal_to_pivot + quick_sort(greater_than_pivot)
