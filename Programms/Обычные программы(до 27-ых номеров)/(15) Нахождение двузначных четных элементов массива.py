s = 0
a = []
print ("Введите первый эллемент массива")
a.append (int(input()))
print ("Введите второй эллемент массива")
a.append (int(input()))
print ("Введите терий эллемент массива")
a.append (int(input()))
print ("Введите четвертый эллемент массива")
a.append (int(input()))
for j in range (4):
    if a [j] //10 != 0 and a [j] % 2 == 0:
        s += 1
print(s)