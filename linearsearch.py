def LSearch(arr,ele):
    size = len(arr)-1
    i=0
    while(i<=size):
        if(arr[i]==ele):
            return i
        i=i+1
list = [1,2,3,4,5,6,7,8]
ele=7
print(LSearch(list,ele))
