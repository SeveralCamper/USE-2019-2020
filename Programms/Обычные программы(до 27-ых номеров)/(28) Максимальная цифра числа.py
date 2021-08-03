a = int (input())
maximum = 0
while a > 0:
    digit = a % 10
    if digit > maximum:
        maximum = digit
    a = a // 10
print (maximum)
