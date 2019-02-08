"""
Quick sort is typically faster than merge sort when the data is stored in memory. 
However, when the data set is huge and is stored on external devices such as a hard drive, merge sort is the clear winner in terms of speed. 
It minimizes the expensive reads of the external drive and also lends itself well to parallel computing.

Partition-Exchange sort
Divide-Conquer technique

Best case: O(n*log2(n)) (Every time pivot moves to the center the the sublists are of equal sizes)
Worst case: O(n*n) (If pivot is the smallest or the largest element of the list for every element in the list)
Unstable sort
Non adaptive sort (Data insensitive - Performance doesn't depend on order of input data) (Not efficient for lists that are almost sorted)
Space complexity: O(log2(n))    #How???
"""

def quick_sort(a):
    n = len(a)
    sort(a, 0, n-1)

def sort(a, low, high):
    if low >= high: #0 or 1 element in sublist
        return

    p = partition(a, low, high)

    sort(a, low, p-1)   #sort left sublist
    sort(a, p+1, high)  #sort right sublist

def partition(a, low, high):
    pivot = a[low]
    i = low+1   #moves from left to right
    j = high    #moves from right to left

    while i<=j:
        while a[i] < pivot and i<high:
            i += 1
        while a[j] > pivot:
            j -= 1

        if i < j:    #swap a[i] and a[j]
            a[i], a[j] = a[j], a[i]
            i += 1
            j -= 1
        else:   #found proper place for pivot
            break

    #Proper place for pivot is j
    a[low] = a[j]
    a[j] = pivot

    return j
            
###############################################################################

list1 = [6,3,7,1,8,2,14,11]
quick_sort(list1)
print(list1)

list2 = [7,6,5,4,43,2,1,11]
quick_sort(list2)
print(list2)

list3 = [6]
quick_sort(list3)
print(list3)

list4 = [1,2,3,4,5,6,7,8,9]
quick_sort(list4)
print(list4)

list5 = [5,4,3,2,1,0]
quick_sort(list5)
print(list5)

list6 = [17,13,9,5,1,14,7,8,16,2,11,15,10,12,6,3,4]
quick_sort(list6)
print(list6)