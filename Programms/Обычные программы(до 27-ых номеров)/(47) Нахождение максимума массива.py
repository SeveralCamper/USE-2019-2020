a = []
N = 10
j = 0
for i in range (N):
    a.append(int(input()))
for i in range (N):
    if a[i] >= 24 and a[i] % 10 == 0:
        if a[i] > j:
            j = a[i]
for i in range (N):
    if a[i] >= 24 and a[i] % 10 == 0:
        a [i] = j
for i in range (N):
    print (N)
