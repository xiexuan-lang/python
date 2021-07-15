n = input().split()
total = 0
for i in range(int(n[0]), int(n[1]) + 1):
    for j in str(i):
        if '2' in j:
            total = total + 1
print(total)
