import random

arr = [0] * 10
for i in range(10):
    arr[i] = random.randint(0,100)

for i in range(1,len(arr)):
    for j in range(i-1,-1,-1):
        if arr[j+1] <= arr[j]:
            arr[j],arr[j+1] = arr[j+1],arr[j]
        else:
            break

print(arr)