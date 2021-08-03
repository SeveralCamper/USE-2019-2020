mult = 1
count = 0
for i in range (4):
    x = int (input())
    if x < 0:
        count += 1
        mult = mult * x
if mult == 1:
    print ("Габелыч")
else:
    print (count)
    print (mult)