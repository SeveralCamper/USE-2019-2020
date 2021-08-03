a = []
N = 2014
j = 0
for i in range (N):
    a.append(int(input()))
for i in range (1,N-1):
    if a[i] > a[i+1] and a[i] > a[i-1]:
        j += a[i]
print (j)
