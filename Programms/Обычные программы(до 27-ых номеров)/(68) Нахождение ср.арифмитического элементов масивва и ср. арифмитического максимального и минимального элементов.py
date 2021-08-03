a = []
N = 30
for i in range(0,N):
    a.append(int(input()))
minimum = a[1]
maximum = a[1]
i = 0
sum = 0
sred1 =float(0)
sred2 =float(0)
for i in range(0,N):
    maximum = max(a)
    minimum = min(a)
    sum += a[i]
sred1 = sum/N
sred2 = (maximum + minimum)/2
print(sred1)
print(sred2)


