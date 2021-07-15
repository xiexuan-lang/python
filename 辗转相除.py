a = input().split()
m, n = int(a[0]), int(a[1])
if m < n:
    m, n = n, m
while m % n != 0:
    m, n = n, m % n
print(n)
