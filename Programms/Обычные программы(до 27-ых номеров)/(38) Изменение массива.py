a = [2, 3, -7, 8, 10, 9, 4, 9, 12, 0]
n = 9
s = 0
for i in range (1, n+1):
    if a[i-1] < a[i]:
        a[i] = a[i] + a[i-1]
        s = s + a[i] - 3
for i in range (n+1):
    print (a[i])
    print (s)