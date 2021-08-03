a = []
N = 5
j = 0
k = 0
for i in range(N):
    a.append(int(input()))
for i in range(N):
    if a[i] % 2 != 0:
        k +=1
for i in range(N):
    if a[i] % 2 != 0:
        j = j + a[i]
j = j // k
print (j)

