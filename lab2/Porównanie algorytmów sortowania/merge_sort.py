import string

def merge_sort(words):
    if len(words) <= 1:
        return words

    mid = len(words) // 2
    left_half = merge_sort(words[:mid])
    right_half = merge_sort(words[mid:])

    sorted_words = []
    i = j = 0

    while i < len(left_half) and j < len(right_half):
        if left_half[i].lower() <= right_half[j].lower():
            sorted_words.append(left_half[i])
            i += 1
        else:
            sorted_words.append(right_half[j])
            j += 1

    sorted_words.extend(left_half[i:])
    sorted_words.extend(right_half[j:])

    return sorted_words
