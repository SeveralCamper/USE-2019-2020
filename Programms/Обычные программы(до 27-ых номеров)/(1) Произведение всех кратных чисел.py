n= int(input('Введите цифру')) # Просим ввести число
mult=1                         # Задаем переменную mult, со значением 1, для накопления произведения
for i in range (1,n+1):        # Задаем через цикл for диапозон, в которм буду происходить действия
    if i % 8 == 0 or i % 6 == 0:  # С помощью оператора if проверяем кратность на 8 и 6
        mult = mult*i                 # Накапливает произведение в переменной mult, если число прошло проверку
print (mult)                   # Выводим произведение на экран
