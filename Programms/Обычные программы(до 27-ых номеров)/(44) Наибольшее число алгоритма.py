x = (int(input()))
L = 0
M = 0
while x > 0:
    L = L + 1
    if x % 2 == 1:
        M = M + (x % 10) // 2
    x = x // 10
print (L)
print (M)

