n = int (input("Введите число")) # Просим ввести число
maximum = 1
while n > 0:      # Цикл будет исполняться пока цифра не станет нулем
    digit = n % 10     # получаем цифру числа (остаток от деления на 10 = последней цифре числа)
    if digit % 2 == 0:   # определям четная ли эта цифра (остаток от деления на 2 сравниваем с нулем)
        if digit > maximum:  # с помощью оператора if проверяем, больше или меньше digit указанного конт-значения
            maximum = digit  # присваиваем параметру maximum значание параметра digit
    n = n // 10    # урезаем исходное значание на разряд
print ("Максимальная цифра:", maximum) # Выводим наибольшую цифру на экран
