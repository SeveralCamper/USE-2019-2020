a = []
k = -1
N = int(input())
for i in range(N):
    a.append(int(input()))
for i in range(N-1):
    for j in range(i+1, N):
        if a[i] + a[j] % 2 != 0 and (a[i] + a[j]) > k:
            k = a[i] + a[j]
R = int(input())
if k == -1:
    print('Контроль не пройден')
else:
    print('Вычисленное контрзанчение:', k)
    if m == R:
        print('Контроль не пройден')
    else:
        print('Контроль пройден')