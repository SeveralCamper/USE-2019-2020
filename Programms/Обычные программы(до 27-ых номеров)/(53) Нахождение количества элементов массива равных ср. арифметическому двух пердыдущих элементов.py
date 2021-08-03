a = []
N = 2016
j = 0
for i in range(0, N):
  a.append(int(input()))
for i in range(N):
    if a [i] == (a[i-1]+a[i-2])/2:
        j += 1
print (j)