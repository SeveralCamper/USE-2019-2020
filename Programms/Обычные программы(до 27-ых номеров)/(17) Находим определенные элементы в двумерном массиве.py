s = 0
g = 0
a = [[0] * 7 in range (7)]
for i in range (7):
    for j in range (7):
        if j > i:
            a [i][j] = j - i
        else:
            a [i][j] = i
        a [i][j] += 1
for i in range (7):
    if 3 == a [i]:
        s += 1
for j in range (7):
    if 3 == a [j]:
        g += 1
print (s + g)