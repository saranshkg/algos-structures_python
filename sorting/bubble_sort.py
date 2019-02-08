"""
n-1 passes for n elements
O(n square)
Less data movement
In-place sort
Stable sort
Adaptive sort (Data sensitive - Performance depends on order of input data) (Efficient for lists that are almost sorted)
"""

def bubble_sort(a):
    n = len(a)
    for i in range(n-1):
        swaps = 0
        for j in range(0, n-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                swaps += 1  # If the number of swaps in a particular pass equals to 0, the data has been sorted. No more passes are required.
        if swaps == 0:
            break

###############################################################################

list1 = [6,3,7,1,8,2,14,11]
bubble_sort(list1)
print(list1)

list2 = [7,6,5,4,43,2,1,11]
bubble_sort(list2)
print(list2)

list3 = [6]
bubble_sort(list3)
print(list3)

list4 = [1,2,3,4,5,6,7,8,9]
bubble_sort(list4)
print(list4)

list5 = [5,4,3,2,1,0]
bubble_sort(list5)
print(list5)

list6 = [17,13,9,5,1,14,7,8,16,2,11,15,10,12,6,3,4]
bubble_sort(list6)
print(list6)