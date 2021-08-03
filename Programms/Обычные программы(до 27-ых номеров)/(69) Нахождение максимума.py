a = []
N = 5
for i in range (N):
    a.append(int(input()))
col = 1
colmax = 1
for i in range (N-2):
    if a[i] < a[i+1]:
        col += 1
    if a[i+2] < a[i+1]:
        colmax = col
        col = 0
print(colmax)
