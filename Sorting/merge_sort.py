"""
Name: Merge Sort
Time: O(n log n)
Space: O(n)
"""

def merge_sort(arr: list, start: int, end: int):
    if start >= end:
        return
    #calculate the midpoint
    mid = (start + end) // 2
    merge_sort(arr, start, mid)
    merge_sort(arr, mid+1, end)
    merge(arr, start, mid ,end)

def merge(arr: list, start: int, mid: int, end: int):
    left_len = mid - start + 1
    right_len = end - mid
    
    left_copy = [0] * left_len
    right_copy = [0] * right_len
    
    for i in range(left_len):
        left_copy[i] = arr[start + i]
    for j in range(right_len):
        right_copy[j] = arr[mid+1+j]
    
    i = j = 0
    k = start
    while i < left_len and j < right_len:
        if left_copy[i] <= right_copy[j]:
            arr[k] = left_copy[i]
            i += 1
        else:
            arr[k] = right_copy[j]
            j += 1
        k += 1   
    while i < left_len:
        arr[k] = left_copy[i]
        i += 1
        k += 1
    while j < right_len:
        arr[k] = right_copy[j]
        j += 1
        k += 1
        
array = [9, 1, 5, 4]
print(array)
merge_sort(array, 0, len(array)-1)
print(f"---------------------\n{array}")
    
