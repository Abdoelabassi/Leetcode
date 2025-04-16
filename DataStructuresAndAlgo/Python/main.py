from typing import List


def merge(a: List, b: List) -> List:
    """merge two sorted lists"""
    i = j = 0
    merged_list = []
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            merged_list.append(a[i])
            i += 1
        else:
            merged_list.append(b[j])
            j += 1
            
    while i < len(a):
        merged_list.append(a[i])
        i += 1
    while j < len(b):
        merged_list.append(b[j])
        j += 1
    return merged_list


def merge_sort(a: List) -> List:
    """merge sort algorithm"""
    if len(a) == 1:
        return a
    mid = int(len(a) / 2)
    first_half = a[:mid]
    second_half = a[mid:]
    half_a = merge_sort(first_half)
    half_b = merge_sort(second_half)
    return merge(half_a, half_b)
    
    
    

a: List = [11, 12, 7, 41, 61, 12, 16, 14]

sorted_list = merge_sort(a)

print("unsorted list: ", a)
print("sorted list: ", sorted_list)
    