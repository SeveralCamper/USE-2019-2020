N = int(input())
a = []
asum = 0
for i in range(N):
    a = (int(input()))
    a.append(a)
for i in range(N):
    for j in range(i+1,N):
        if a[i] * a[j] % 27 == 0:
            asum += 1
if asum == 0:
    print('-1')
else:
    print(asum)