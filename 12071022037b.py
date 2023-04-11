
def bubble_sort(arr):
    size = len(arr)
    for i in range(size - 1):
        swapped = False
        for j in range(size - 1 - i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break

ele1 = [11,66,44,55,22,33,88,99,77]
ele2=[11,22,33,44,55]
bubble_sort(ele1)
bubble_sort(ele2)
print(ele1)
print(ele2)
