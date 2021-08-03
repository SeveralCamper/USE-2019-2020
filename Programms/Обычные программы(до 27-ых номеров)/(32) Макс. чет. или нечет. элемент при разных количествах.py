N = 8
a = []
for i in range (N):
    a.append (int(input()))
j  = 0
k = 0
for i in range (N):
    if a [i] % 2 == 0:
        k += 1
if k < 8 - k:
    for i in range (N):
        if a [i] % 2 != 0 and a [i] > j:
            j = a [i]
    print (j)
else:
    for i in range (N):
        if a [i] % 2 == 0 and a [i] > j:
            j = a [i]
    print (j)