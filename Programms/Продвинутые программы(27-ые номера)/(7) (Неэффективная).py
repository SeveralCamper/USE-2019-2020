N = (int(input()))
amult = 0
min = 10001
a = []
for i in range(N):
    for j in range(i-4,N):
        if a[i] * a[j] % 2 != 0 and a[i] * a[j] < min:
            amult = a[i] * a[j]
if amult == 0:
    print('-1')
else:
    print(amult)