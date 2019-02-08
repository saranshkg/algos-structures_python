"""
n-1 passes for n elements
O(n square)
Less data movement
In-place sort
Unstable sort
Non adaptive sort (Data insensitive - Performance doesn't depend on order of input data) (Not efficient for lists that are almost sorted)
Efficient when comparison operation is costly
"""

def selection_sort(a):
    n = len(a)
    for i in range(n-1):
        minIndex = i
        for j in range(i+1, n):
            if a[j] < a[minIndex]:
                minIndex = j
        if i!=minIndex:
            a[i], a[minIndex] = a[minIndex], a[i]

###############################################################################

list1 = [6,3,7,1,8,2,14,11]
selection_sort(list1)
print(list1)

list2 = [7,6,5,4,43,2,1,11]
selection_sort(list2)
print(list2)

list3 = [6]
selection_sort(list3)
print(list3)

list4 = [1,2,3,4,5,6,7,8,9]
selection_sort(list4)
print(list4)

list5 = [5,4,3,2,1,0]
selection_sort(list5)
print(list5)

list6 = [17,13,9,5,1,14,7,8,16,2,11,15,10,12,6,3,4]
selection_sort(list6)
print(list6)