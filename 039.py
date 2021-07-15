a = int(input())
ESD = 0
for i in range(a):
    k = 0
    l = input().split()
    s1, s2 = l[0], l[1]
    for j in range(0, len(s1), 1):
        if s1[j] == s2[ESD]:
            ESD = ESD + 1
        else:
            ESD = 0
        if ESD == len(s2):
            print(j - len(s2) + 1, end=" ")
            ESD = 0
            k = 1
    if k == 0:
        print("no", end="")
    print("\n", end="")
