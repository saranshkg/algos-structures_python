"""
After halving the list log2(n) times we get n sublists of size 1
In each pass, n elements are merged
O(n*log2(n))
No an in-place sort
Stable sort
Non adaptive sort (Data insensitive - Performance doesn't depend on order of input data) (Not efficient for lists that are almost sorted)
"""

def merge_sort(a):
    n = len(a)
    temp = [None] * n
    size = 1
    while size <= n-1:
        sort_pass(a, temp, size, n)
        size = size * 2

def sort_pass(a, temp, size, n):
    low1 = 0
    while low1 + size <= n-1:
        high1 = low1 + size - 1
        low2 = low1 + size
        high2 = low2 + size - 1

        if high2 >= n:  #if length of last sublist is less than size
            high2 = n-1

        merge(a, temp, low1, high1, low2, high2)

        low1 = high2 + 1    #take next two sublists for merging

    for i in range(low1, n):
        temp[i] = a[i]

    copy(a, temp, n)

#a[low1]...a[high1] and a[low2]...a[high2] merged to temp[low1]...temp[high2]
def merge(a, temp, low1, high1, low2, high2):
    i = low1
    j = low2
    k = low1

    while i<=high1 and j<=high2:
        if a[i] < a[j]:
            temp[k] = a[i]
            i += 1
        else:
            temp[k] = a[j]
            j += 1
        k += 1

    while i<=high1:
        temp[k] = a[i]
        i += 1
        k += 1

    while j<=high2:
        temp[k] = a[j]
        j += 1
        k += 1

#copies temp to a
def copy(a ,temp, n):
    for i in range(n):
        a[i] = temp[i]

###############################################################################

list1 = [6,3,7,1,8,2,14,11]
merge_sort(list1)
print(list1)

list2 = [7,6,5,4,43,2,1,11]
merge_sort(list2)
print(list2)

list3 = [6]
merge_sort(list3)
print(list3)

list4 = [1,2,3,4,5,6,7,8,9]
merge_sort(list4)
print(list4)

list5 = [5,4,3,2,1,0]
merge_sort(list5)
print(list5)

list6 = [17,13,9,5,1,14,7,8,16,2,11,15,10,12,6,3,4]
merge_sort(list6)
print(list6)