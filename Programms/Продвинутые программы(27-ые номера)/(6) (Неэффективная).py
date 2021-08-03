a = []
maximum = 0
N = (int(input()))
for i in range(N):
    a.append(int(input()))
for i in range(N):
    for j in range(i+1,N):
        if i < j and a[i] > a[j]:
            if a[i] + a[j] % 3 == 0 and a[i] + a[j] > maximum:
                maximum = a[i] + a[j]
print(maximum)