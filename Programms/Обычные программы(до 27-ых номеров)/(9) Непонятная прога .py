def F(x):
    return (x-5) * (x+12) + 40
M = 1
R = F(1)
for t in range (1,4):
    if F(t) > R:
        M=t
        R = F(t)
print (M+R)
