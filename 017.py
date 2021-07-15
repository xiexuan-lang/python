a = input().split()
n, m, w = int(a[0]), int(a[1]), str(a[2])
if w == '+':
    print(n + m)
elif w == '-':
    print(n - m)
elif w == '*':
    print(n * m)
elif w == '/':
    if m == 0:
        print("Divided by zero!")
    else:
        print(int(n / m))
else:
    print("Invalid operator!")
