a = []
N = 10
k = a[0]
for i in range(0,N):
    a.append(int(input()))
for i in range(1,N-1):
        if a[i] < a[i+1] and a[i] < a[i-1]:
            if a [i] < k:
                k = a[i]
if k == a[0]:
    print("0")
else:
    print(k)