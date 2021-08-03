a = []
N = 2000
i = 0
k = 0
for i in range(0,N):
    a.append(int(input()))
for i in range(0,N):
    i += a[i]
if i % 2 == 0:
    for i in range (0,N):
        if a[i] % 2 == 0:
            k += a[i]
else:
    for i in range (0,N):
        if a[i] % 2 == 0:
            k += a[i]
print (k)