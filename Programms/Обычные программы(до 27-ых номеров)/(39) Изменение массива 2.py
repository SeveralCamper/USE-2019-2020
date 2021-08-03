a = [4, 2, 9, 0, 0, -1, -3, 9, 8, 4]
s = 0
for i in range(1,9,2):
    s += a[i-1] + a[i+1]
    print(s)
for i in range(0,10,2):
    s -= a[i]
    print (s)
s *= a[9]
print(s)