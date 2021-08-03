n = int(input())
k = 0
while n % 5 == 0:
    k = k + 1
    n = n // 5
if n > 0:
    print (k)
else:
    print ("Не существует")