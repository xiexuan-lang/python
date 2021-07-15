a = input().split(',')
s, s1, s2 = a[0], a[1], a[2]
EDS1 = winA = winB = 0
EDS2 = len(s2)-1
if (s1 not in s or s2 not in s) or (s == s1 == s2):
    print("-1")
    exit(0)
for i in range(0, len(s)-1, 1):
    if s1[EDS1] == s[i]:
        EDS1 += 1
    else:
        EDS1 = 0
    if EDS1 == len(s1):
        winA = i
        break

for j in range(len(s)-1, 0, -1):
    if s2[EDS2] == s[j]:
        EDS2 -= 1
    else:
        EDS2 = len(s2)-1
    if EDS2 < 0:
        winB = j-1
        break
if winB < winA:
    print("-1")
else:
    print(winB - winA)
