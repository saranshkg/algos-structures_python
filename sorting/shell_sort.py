"""
Improved version of insertion sort
Diminishing increment sort
Running time depends on number of increments and their values
Many movements
In-place sort
Unstable sort
Adaptive sort (Data sensitive - Performance depends on order of input data) (Efficient for lists that are almost sorted)

Here, when h is large, it implies that the sublists are small ( small value of n of sublists) => Hence efficiency of insertion sort in these cases increases.
Also, when h is small, it implies that the sublists are large (they have become almost sorted) => Hence efficiency of insertion sort in these cases also increases.
Thus, overall shell sort becomes an improved version of insertion sort.

Choice of increment:
    h can be any value at initiation and reduce by any factor but should end at 1.
    However, increments that are multiples of each other (Ex: 1, 3,6,9 or 1,2,4,8) are a bad choice since until the last pass, only odd elements are grouped together ann even ones together.
    Increments which are relatively prime are a good choice.

    Increments given by Knuth:
        h(1) = 1, h(i+1) = 3*h(i) + 1
        Stop at h(i) when h(i) > (n-1)/9
        Ex:
            If n = 10000, then increments would be:
                1
                4
                13
                40
                121
                364
                1093
                3280
"""

def shell_sort(a):
    n = len(a)
    h = int(input("Enter maximum increment (odd value) : "))
    while h >= 1:
        for i in range(h, n):
            tmp = a[i]
            j = i - h
            while j>=0 and a[j] > tmp:
                a[j+h] = a[j]
                j -= h
            a[j+h] = tmp
        h -= 2
        
###############################################################################

list1 = [6,3,7,1,8,2,14,11]
shell_sort(list1)
print(list1)

list2 = [7,6,5,4,43,2,1,11]
shell_sort(list2)
print(list2)

list3 = [6]
shell_sort(list3)
print(list3)

list4 = [1,2,3,4,5,6,7,8,9]
shell_sort(list4)
print(list4)

list5 = [5,4,3,2,1,0]
shell_sort(list5)
print(list5)

list6 = [17,13,9,5,1,14,7,8,16,2,11,15,10,12,6,3,4]
shell_sort(list6)
print(list6)