# -*- coding: utf-8 -*-


def quicksort(a_list, first, last):
    if first < last:
        split = partition(a_list, first, last)
        quicksort(a_list, first, split-1)
        quicksort(a_list, split+1, last)

def partition(a_list, first, last):
    pivot_value = a_list[first]
    left = first + 1
    right = last
    
    done = False
    while not done:
        while left <= right and a_list[left] <= pivot_value:
            left += 1
        while left <= right and a_list[right] >= pivot_value:
            right -= 1

        if right < left:
            done = True
        else:
            a_list[left], a_list[right] = a_list[right], a_list[left]

    a_list[first], a_list[right] = a_list[right], a_list[first]

    return right

if __name__ == '__main__':
    a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    quicksort(a_list, 0, len(a_list)-1)
    print a_list
