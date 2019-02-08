def merge(a1, a2, temp):
    i=0
    j=0
    k=0

    while i<=n1-1 and j<=n2-1:
        if a1[i] < a2[j]:
            temp[k] = a1[i]
            i += 1
        else:
            temp[k] = a2[j]
            j += 1
        k += 1

    while i<=n1-1:
        temp[k] = a1[i]
        i += 1
        k += 1

    while j<=n2-1:
        temp[k] = a2[j]
        j += 1
        k += 1
    
###############################################################################

n1 = int(input("Enter the number of elements in list a1 : "))
print("Enter the elements in ascending order")
a1 = [None]*n1
for i in range(n1):
    a1[i] = int(input("Enter the element : "))
    
n2 = int(input("Enter the number of elements in list a2 : "))
print("Enter the elements in ascending order")
a2 = [None]*n2
for i in range(n2):
    a2[i] = int(input("Enter the element : "))

temp = [None] * (n1 + n2)
merge(a1, a2, temp)
print("Merged list temp is : ", temp)