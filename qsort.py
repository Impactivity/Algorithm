import random
data_list = random.sample(range(100),10)

def qsort(x):
    if len(x) <= 1: return x
    pivot, left,right = x[0], [],[]

    left = [data for data in x[1:] if data < pivot]
    right = [data for data in x[1:] if data >= pivot]
    return qsort(left) + [pivot] + qsort(right)

print(qsort(data_list))




