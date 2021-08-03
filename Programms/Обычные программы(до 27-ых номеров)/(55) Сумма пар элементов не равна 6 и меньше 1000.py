a = []
N = 40
j = 0
for i in range(N):
    a.append(int(input()))
for i in range(N):
    if (a[i] + a[i+1]) % 6 != 0 and a[i] * a[i+1] < 1000:
        j += 1
print (j)
