a = []
n = 5
for i in range (n):
    a.append (int(input()))
k = 0
for i in range (1, n):
    if (a[i-1] + a[i]) % 3!=0 and a[i-1]*a[i] <= 512:
        k += 1
print(k)