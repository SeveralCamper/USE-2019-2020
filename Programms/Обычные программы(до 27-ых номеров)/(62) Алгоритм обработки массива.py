a = [3, 2, 4, 6, 3, 10, 12, 14, 16, 18]
c = 0
t = 0
for i in range(1,9):
    if a[i] == a[0]:
        c += 1
        t=a[i+1]
        a[i+1]= a[i]
        a[i]= t
print(c)
for i in range (9):
    print (a[i])


