N = int(input())
s = 0
mx = -1000
for i in range(N):
    x = int(input())
    if x < 0:
        s =+ x
    if x > mx:
        mx = x
print (mx,x)
