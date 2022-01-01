n = int(input())

data = list(map(int, input().split()))

def binary_search(array, start, end):
    if start > end:
        return -1
    
    mid = (start + end) // 2

    if mid == array[mid]:
        return mid
    elif mid < array[mid]:
        return binary_search(array, start, mid-1)
    else:
        return binary_search(array, mid+1, end)
    
print(binary_search(data, 0, n-1))