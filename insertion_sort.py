import sys
read = sys.stdin.readline

arr = [5,3,2,6,7,8,1,9]

def insertion_sort(arr):
    n = len(arr)

    for i in range(1,n):
        here = i - 1
        key = arr[i]
        while here >= 0 and key < arr[here] :
            arr[here+1] = arr[here]
            here -= 1
        arr[here+1] = key

    return arr

print(insertion_sort(arr))