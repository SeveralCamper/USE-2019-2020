s1 = 'trigger'

s2 = 'programming'

s3 = s1[: s2.count('m') * 4 - 2] + s2[1 : s2.count('m') * 3 + s1.count('g')*2 : 2]

print(s3)
