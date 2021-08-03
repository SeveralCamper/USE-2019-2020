a = int(input())
count = 0
while a > 0:
    digit = a % 10
    if digit % 4 == 0:
        count += 1
    a = a //10
if count == 0:
    print ("Габелыч")
else:
    print (count)
