array = [10,5,2,3,4,8,6,1]
def quick_sort(array,start,end):
    if start >= end:
        return
    pivot = start
    left , right = start + 1 , end

    while left <= right:
        while left <= end and array[left] <= array[pivot]:
            left += 1
        while right > start and array[right] >= array[pivot]:
            right -= 1
        print(left, right)
        if left > right :
            array[right] , array[pivot] = array[pivot] , array[right]
        else:
            array[right] , array[left] = array[left], array[right]
    print(array)
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)

# print(array)
# quick_sort(array,0,len(array) - 1)
# print(array)


def quicksort(x, low, high):
    if low >= high:
        return

    pivot = low

    divide = part(x, pivot,high)

    quicksort(x,low,divide-1)
    quicksort(x,divide+1, high)

def part(x, pivot, high):
    i = pivot + 1
    j = high
    while i <= j:
        while i <= high and x[i] <= x[pivot]:
            i += 1

        while j > pivot and x[j] >= x[pivot]:
            j -= 1
            if i > j:
                break

        if i <= j:
            x[i], x[j] = x[j], x[i]

    x[pivot], x[j] = x[j], x[pivot]

    return j

quicksort(array,0,len(array)-1)

print(array)