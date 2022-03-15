import sys

read = sys.stdin.readline

input_list = list(map(int, read().split()))

def quick_sort( arr ):

    if len(arr) <= 1 :
        return arr

    # pivot 값을 중간 값으로 지정했을 때 구현.
    pivot = arr[len(arr) // 2]
    left_arr ,equal_arr, right_arr = [],[],[]

    for i in arr :
        if i < pivot: # pivot보다 작으면 왼쪽
            left_arr.append(i)
        elif i > pivot: # pivot보다 크면 오른쪽
            right_arr.append(i)
        else:
            equal_arr.append(i)

    return quick_sort(left_arr) + equal_arr + quick_sort(right_arr)


print(quick_sort(input_list))


