a = []
N = 30
j = 0
for i in range(N):
    a.append(int(input()))
for i in range (N):
    if a[i] > 1002 and a[i] % 3 == 0:
        j += 1
for i in range (N):
    if a[i] > 1002 and a[i] % 3 == 0:
        a [i] = j
for i in range (N):
    print (a[i])
