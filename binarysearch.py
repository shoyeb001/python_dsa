def BinarySearch(arr,ele):
    start = 0
    end = len(arr)-1
    while(start<=end):
        mid=(start+end)//2
        if(arr[mid]==ele):
            return mid
        elif(ele<arr[mid]):
            end = mid-1
        else:
            start = mid+1

list = [2,3,4,5,6,7,8]
ele=3
print(BinarySearch(list,ele))
