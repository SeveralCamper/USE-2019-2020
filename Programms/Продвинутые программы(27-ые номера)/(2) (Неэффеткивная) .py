# На вход поступает последовательность из N положительных числел, все числа последовательности различны. Рассматриваются все пары различных элементов последовательности. Необходимо определить
# Необходимо определить количество пар, для которых произведение элементов не кратно 14. В первой строке данных задается количество чисел N (1 <= N <= 1000). В каждой из последующих N строк
# записано одно целое положительное число, не превыщающее 1000. В качестве результата программа должна напечатать одно число: количество пар, в которых произведение элементов не кратно 14
a = []
k = 0
N = int(input())
for i in range(N):
    a.append(int(input()))
for i in range(N-1):
    for j in range(i+1, N):
        if a[i] * a[j] % 14 != 0:
            k = k + 1
print(k)