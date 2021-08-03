a = []
N =20
j = 1001
for i in range (N):
    a.append(int(input()))
for i in range (N):
    if a[i] >= 0 and a[i] % 2 == 0:
        if a[i] < j:
            j = a[i]
if j == 1001:
    print ("Не найдено")
else:
    print (j)