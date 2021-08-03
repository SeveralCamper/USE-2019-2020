a = []
s = 0
x = 0
y = 0
N = (int(input()))
for i in range(N):
    a.append(int(input()))
for i in range(n-6):
    for g in range(i+6,n):
        if a[i] > a[g]:
            if a[i] + a[g] > 343:
                s = a[i] + a[g]
                x = a[i]
                y = a[g]
if s != 0:
    print(s)
    print(x)
    print(y)
else:
    print("Баста, карапузики!")
