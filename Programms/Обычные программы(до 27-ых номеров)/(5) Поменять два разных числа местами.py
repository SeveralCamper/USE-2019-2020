a = int (input("Введите одно из чисел: 10 либо 40"))
b = int (input("Введите отличное от первого число: 10 либо 40"))
if a > b:    # 
    a = a // b # a = 4
    b = b * a  # b = 40
    a = b // a # a = 10
    print (a,b)
else:
    b = b // a # b = 4
    a = a * b  # a = 40
    b = a // b # b = 10
    print (a,b)



