# -*- coding: utf-8 -*-


def mergesort(a_list):
    if len(a_list) == 1:
        return

    mid = len(a_list) / 2
    left = a_list[:mid]
    right = a_list[mid:]

    mergesort(left)
    mergesort(right)

    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            a_list[k] = left[i]
            i += 1
        else:
            a_list[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        a_list[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        a_list[k] = right[j]
        j += 1
        k += 1

if __name__ == '__main__':
    a_list = [54,26,93,17,77,31,44,55,20]
    mergesort(a_list)
    print a_list
