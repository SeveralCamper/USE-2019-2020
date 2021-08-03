N = 8
a = []
for i in range (N):
    a.append (int(input()))
k = 0
for i in range (N):
    if a [i] >= 154 and a [i] <= 255 and a [i] % 16 > 9:
        k = k + 1
print (k)