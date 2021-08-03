maximum = 1
a = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for n in range (10):
    a [n] = (n + 25)
for n in range (10):
    b [9-n] = a [n]
for index in range (10):
    s = b [9-n]
    if s > maximum:
        maximum = s
print ("Наибольшее значение это:", maximum)