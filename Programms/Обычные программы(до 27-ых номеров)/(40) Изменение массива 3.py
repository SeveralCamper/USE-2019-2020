a = [1, 2, 5, 8, 9, 3, 4, 0, 7, 6]
n = 10
for i in range(n-1):
    for j in range(n - i - 1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
for i in range (n):
    print (a[i])


