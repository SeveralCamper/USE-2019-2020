N = 30
a = []
maximum = 0
for i in range (N):
    a.append (int(input()))
    for j in range (N):
        if a [j] % 10 == 4:
            if a [j] > maximum:
                maximum = a [j]
if maximum == 0:
    print ("Ничего не найдено")
else:
    print (maximum)

