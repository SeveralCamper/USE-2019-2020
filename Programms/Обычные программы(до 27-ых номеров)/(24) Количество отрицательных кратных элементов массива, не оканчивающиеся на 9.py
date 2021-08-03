N = 40
a = []
for i in range (N):
    a.append (int(input()))
j = 0
for k in range (41):
    if a [k] > -1000 and a [k] < -99:
        if a [k] % 10 == 9 and a [k] % 3 == 0:
            j = j + 1
print (j)