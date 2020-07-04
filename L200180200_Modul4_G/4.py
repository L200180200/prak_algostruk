def binarySearch(kumpulan,target):
    low = 0
    high = len(kumpulan) - 1
    #print(len(kumpulan))

    while low <= high:
        mid = (high + low) // 2
        if kumpulan[mid] == target:
            return True
        elif target < kumpulan[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return False

llist = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print(binarySearch(llist,20))
print(binarySearch(llist,10))
