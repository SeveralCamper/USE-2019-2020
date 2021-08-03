a = []
N = 2016
m = 0
for i in range(0, N):
    a.append(int(input()))
for i in range (N):
    if a [i] % 16 == 11:
        if a [i] > m:
            m = a[i]
if m == 0:
    print (0)
else:
    print (m)
    