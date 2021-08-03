N = 8
a = []
for i in range (N):
    a.append (int(input()))
k = 0
for i in range (N):
    if a [i] > 99 and a [i] < 1000:
        if a [i] % 10 == 3:
            k = k + a [i]
for i in range (N):
    if a[i] > 99 and a[i] < 1000:
        if a[i] % 10 == 3:
            a [i] = k
for i in range (N):
    print (a [i])