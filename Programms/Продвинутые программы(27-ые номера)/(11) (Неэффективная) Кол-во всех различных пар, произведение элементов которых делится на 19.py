# На вход программы поступает последовательность из N целых положительных чисел, все
# числа в последовательности различны. Рассматриваются все пары различных элементов
# последовательности, находящихся на расстоянии не меньше чем 4 (разница в индексах
# элементов пары должна быть 4 или более, порядок элементов в паре неважен). Необходимо определить количество таких пар, для которых произведение элементов делится на 19.
# В первой строке входных данных задаётся количество чисел N (5 ≤ N ≤ 1000). В каждой из
# последующих N строк записано одно целое положительное число, не превышающее 10000.
# находящихся в последовательности на расстоянии не меньше чем 4, в которых произведение элементов кратно 19.
k = 0
a = []
n = int(input())
for i in range(n):
    a.append(int(input()))
for i in range(n - 4):
    for j in range(i + 4, n):
        if a[i]*a[j]%19==0:
            k+=1
print(k)