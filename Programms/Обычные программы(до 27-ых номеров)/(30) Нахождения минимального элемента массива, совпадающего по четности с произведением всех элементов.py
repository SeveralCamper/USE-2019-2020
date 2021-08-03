N = 10
a = [10, 2, 15, 345, 32, 41, 17, 9, 38, 503, 61]
minimum = 1001
mult = 1
for i in range(N + 1):
    mult = mult * a[i]
if mult % 2 == 0:
    for i in range(N + 1):
        if a[i] < minimum and a[i] % 2 == 0:
            minimum = a[i]
    print(minimum)
else:
    if mult % 2 != 0:
        for i in range(N + 1):
            if a[i] < minimum and a[i] % 2 != 0:
                minimum = a[i]
    print(minimum)