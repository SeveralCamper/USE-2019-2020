N = 8
a = []
for i in range (N):
    a.append (int(input()))
k = 0
for i in range (N-2):
    if a [i] == ((a [i+1] + a [i+2]) / 2):
        k = k + 1
print (k)
