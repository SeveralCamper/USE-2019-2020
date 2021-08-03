N = 40
a = []
minimum = 1001
for i in range (N):
    a.append(int(input()))
    for j in range (41):
        if a [j] > 9 and a [j] < 100:
            if a [j] % 5 != 0:
                if a [j] < minimum:
                    minimum = a [i]
if minimum == 1001:
    print ("Не найдено")
else:
    print (minimum)