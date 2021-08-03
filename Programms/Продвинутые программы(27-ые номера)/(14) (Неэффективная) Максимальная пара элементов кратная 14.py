a = []
N = int(input())
maximum = -1
p1 = 0
p2 = 0
for i in range (N):
    a.append(int(input()))
for i in range(N-1):
    for j in range(i+1,N):
        if a[i] * a[j] % 14 == 0 and a[i] * a[j] > maximum:
            p1 = a[i]
            p2 = a[j]
            maximum = a[i] * a[j]
contr = int(input())
if maximum == contr:
    print (p1)
    print (p2)
else:
    print ('Контроль не пройден')
    print ('NO')

