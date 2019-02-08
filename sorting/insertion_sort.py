"""
n-1 passes for n elements
O(n square)
Many movements
In-place sort
Stable sort
Efficient when n is small
Adaptive sort (Data sensitive - Performance depends on order of input data) (Efficient for lists that are almost sorted)
"""

def insertion_sort(a):
    n = len(a)
    for i in range(1, n):
        tmp = a[i]
        j = i - 1
        while j>=0 and a[j] > tmp:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = tmp
        
###############################################################################

list1 = [6,3,7,1,8,2,14,11]
insertion_sort(list1)
print(list1)

list2 = [7,6,5,4,43,2,1,11]
insertion_sort(list2)
print(list2)

list3 = [6]
insertion_sort(list3)
print(list3)

list4 = [1,2,3,4,5,6,7,8,9]
insertion_sort(list4)
print(list4)

list5 = [5,4,3,2,1,0]
insertion_sort(list5)
print(list5)

list6 = [17,13,9,5,1,14,7,8,16,2,11,15,10,12,6,3,4]
insertion_sort(list6)
print(list6)