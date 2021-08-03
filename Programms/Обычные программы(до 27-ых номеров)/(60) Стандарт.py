a = []
N = 40
for i in range(N):
    a.append(int(input()))
j = 10001
for i in range(N):
    if a[i] % 10 == 0:
        if a[i] < j:
            j = a[i]
for i in range (N):
    if a[i] % 10 == 0:
        a[i] = j
for i in range(N):
    print(a[i])