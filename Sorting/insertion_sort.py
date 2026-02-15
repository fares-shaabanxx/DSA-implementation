"""
Name: Insertion Sort
Time: O(n^2)
Space: O(1)
"""

def insertion_sort(arr: list[int]):
    for i in range(1, len(arr)):
        key = arr[i] 
        j = i - 1   
        while j >= 0:
            if arr[j] > key:    
                arr[j+1] = arr[j]   
                j -= 1  
            else: break
        arr[j+1] = key      


arr = [9, 1, 5, 4]
insertion_sort(arr)
print(arr)
        
