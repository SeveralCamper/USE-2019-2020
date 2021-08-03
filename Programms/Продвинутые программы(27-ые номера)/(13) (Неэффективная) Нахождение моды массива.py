# Дед Мороз и Снегурочка приходят на детские утренники с мешком конфет.
# Дед Мороз делит конфеты поровну между всеми присутствующими детьми (детей на утреннике никогда не бывает больше 100), а оставшиеся конфеты отдает Снегурочке.
# Снегурочка каждый раз записывает в блокнот количество полученных конфет. Если конфеты разделились между всеми детьми без остатка, Снегурочка ничего не получает и ничего не записывает.
# Когда утренники закончились, Деду Морозу стало интересно, какое число чаще всего записывала Снегурочка.
# Дед Мороз и Снегурочка — волшебные, поэтому число утренников N, на которых они побывали, может быть очень большим.
# Напишите программу, которая будет решать эту задачу.
# Перед текстом программы кратко опишите алгоритм решения задачи и укажите используемый язык программирования и его версию.

N = (int(input()))
a = []
for i in range (N):
    D = (int(input()))
    K = (int(input()))
    if K % D != 0:
        a.append(K % D)
    else:
        a.append(0)
print(a)

a_set = set (a)
most_common = None
qty_most_common = 0

for item in a_set:
    qty = a.count(item)
    if qty > qty_most_common:
        qty_most_common = qty
        most_common = item
print(most_common)