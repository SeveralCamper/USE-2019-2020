a = [54, 34, 21, 567, 32, 56, 78, 11, 4, 9, 34, 97, 3, 2, 1]
maximum = 9
for i in range (N):
    if a [i] > 10 and a [i] < 99 and a [i] % 7 == 0 and a [i] % 3 != 0 and a [i] > maximum:
        maximum = a [i]
    if maximum > 9:
        print (maximum)
    else:
        print ("Не найдено")

