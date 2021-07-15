a = input().split()
n, x, y = int(a[0]), int(a[1]), int(a[2])
if y % x == 0:
    if y/x > n:
        print("0")
    else:
        print(n - int(y / x))
else:
    if y/x > n:
        print("0")
    else:
        print(n - int(y / x) - 1)
