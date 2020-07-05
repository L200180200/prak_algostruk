from kegiatanModul5 import *

A = [1,2,3,10,11,12]
B = [4,5,6,7,8,9]

def urutGabung(list1, list2):
    C = list1 + list2
    insertionSort(C)
    return C
