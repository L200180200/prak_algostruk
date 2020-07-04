def cariTerkecil(kumpulan):
	n = len(kumpulan)
	terkecil = kumpulan[0]
	for i in range(1,n):
		if kumpulan[i] < terkecil:
			terkecil = kumpulan[i]
	print (terkecil)

def cariLurus(wadah, target):
	n = len(wadah)
	for i in range(n):
		if wadah[i] == target:
			return True
	return False

def binSe(kumpulan,target):
    low = 0
    high = len(kumpulan) - 1
    #print(len(kumpulan))

    while low <= high:
        mid = (high + low) // 2
        if kumpulan[mid] == target:
            return kumpulan[mid]
        elif target < kumpulan[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return False



k = [4,5,6]
cariTerkecil(k)
