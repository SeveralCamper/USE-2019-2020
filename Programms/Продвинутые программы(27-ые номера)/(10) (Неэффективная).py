N = (int(input()))
m = 0
a = []
for i in range(N):
    a.append(int(input()))
for i in range (N):
    for j in range(i-1,N):
        if a[i] * a[j] != 34:
            m += 1
print (m)
