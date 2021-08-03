a = []
N = 30
j = 0
for i in range(N):
    a.append(int(input()))
for i in range(N):
    if a[i] % 10 == 4:
        j +=1
for i in range(N):
    if a[i] % 10 == 4:
        a[i] = j
for i in range(N):
    print(a[i])