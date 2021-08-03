count = 0
multiply = 1
N = int(input())
for i in range (N):
    x = int(input())
    if x < 0:
        count += 1
        multiply = multiply * x
print (count)
print (multiply)
