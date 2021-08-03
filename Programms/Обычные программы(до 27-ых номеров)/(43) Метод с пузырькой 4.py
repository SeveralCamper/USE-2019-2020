N = 10
a = [1, 2, 5, 8, 9, 3, 4, 0, 7, 6]
for i in range(N-1):
    for j in range(N - i - 1):
        if a[j] < a[j - 1]:
            a[j], a[j - 1] = a[j - 1], a[j]
print(a)