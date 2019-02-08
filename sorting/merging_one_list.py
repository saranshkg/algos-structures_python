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

###############################################################################

a = [1,2,4,6,  3,5,6,7,13,19]

temp = [None] * len(a)
merge(a, temp, 0, 3, 4, 9)
print("Merged list temp is : ", temp)        