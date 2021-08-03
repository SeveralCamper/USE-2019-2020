a = [ 1, 2, 4, 5, 7, 9, 6, 8, 0, 3]
j = 5
while a[j] > a[j + 1]:
    a[j],a[j + 1] = a[j + 1],a[j]
    j -= 1
    print (j)