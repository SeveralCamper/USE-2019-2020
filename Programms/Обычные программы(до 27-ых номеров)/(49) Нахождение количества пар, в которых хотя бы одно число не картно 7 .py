a = []
N = 30
j = 0
k = 0
for i in range(N):
    a.append(int(input()))
for i in range (N):
    if a[i] % 7 != 0 or a[i+1] % 7 != 0:
        k += 1
print (k)


