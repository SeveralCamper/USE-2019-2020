s = input()
s = s[:-1]
a = [0]*26
for i in range (len(s)):
    a[ord(s[i])-ord('a')] += 1
for  i in range (26):
    if a[i] == 0:
        a[i] = 10001
m = min(a)
s = ''
while m != 10001:
    s += chr(a.index(m)+ord('a'))
    m = min(a)
print(s)
