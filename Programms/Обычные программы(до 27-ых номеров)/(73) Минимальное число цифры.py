n = int(input())
minimum = 9
while n > 0:
    digit = n % 10
    if digit < minimum:
        minimum = digit
    n //= 10
print (minimum)
