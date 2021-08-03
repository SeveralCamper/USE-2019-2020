a = []
N = 5
k = 0
for i in range(N):
    a.append(int(input()))
while k < 3:
    for i in range (N):
        if a[i] > 0:
            k += 1
        if k == 3:
            break
print (a[i])

