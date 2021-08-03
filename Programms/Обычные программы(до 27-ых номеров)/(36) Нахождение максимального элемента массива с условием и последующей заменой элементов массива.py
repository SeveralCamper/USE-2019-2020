N = 8
a = []
for i in range (N):
    a.append (int(input()))
k = 0
for i in range (N):
    if a [i] % 3 == 0 and a [i] % 8 != 0:
        if a [i] > k:
            k = a [i]
for i in range (N):
    if a [i] % 3 == 0 and a [i] % 8 != 0:
        a [i] = k
for i in range (N):
    print (a [i])


