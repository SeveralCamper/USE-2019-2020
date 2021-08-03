N = 8
a = []
for i in range (N):
    a.append (int(input()))
j = 0
k = 0
for i in range (N):
    j = j + a [i]
if j % 2 == 0:
    for i in range (N):
        if a [i] % 2 != 0:
            k = k + 1
    print (k)
if j % 2 != 0:
    for i in range (N):
        if a [i] % 2 == 0:
            k = k + 1
    print (k)