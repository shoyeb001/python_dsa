def BubbleSort(arr,n):
    for i in range (n-1):
        for j in range(n-i-1):
            if(arr[j]>arr[j+1]):
                arr[j],arr[j+1]=arr[j+1],arr[j]

arr = [1,4,2,3,6]
BubbleSort(arr,len(arr))
for i in arr:
    print(i)
