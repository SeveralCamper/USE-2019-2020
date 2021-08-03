a = []
n = int(input())
for i in range (n):
    a.append(int(input()))
max = 0
count = 0
for i in range(n):
    while a[i+1] > a[i]:
        count += 1
        if a [i+1] < a[i]:
            break
    if count > max:
        max = count
        count = 0
print (max)

