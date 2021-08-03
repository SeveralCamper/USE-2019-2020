N = int(input())
a = []
count = 0
multiply = 1
for i in range(N):
    a.append(int(input()))
for i in range(N):
    if a[i] >= 0:
        count += 1
        multiply = multiply * a[i]
if count > 0:
    print(count)
    print(multiply)
else:
    print ('NO')
