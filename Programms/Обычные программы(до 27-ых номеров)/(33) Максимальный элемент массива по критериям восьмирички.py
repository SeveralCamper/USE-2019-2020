N = 8
a = []
for i in range (N):
    a.append (int(input()))
k = 0
j = 0
for i in range (N):
    if a [i] > 512 and a [i] % 8 == 4:
        if a [i] > k:
            k = a [i]
print (k)
