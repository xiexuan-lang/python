n = int(input())
t = 0
if n >= 0:
    while n:
        t *= 10
        t += n % 10
        n //= 10
    print(t)
else:
    while n:
        t = 10 * t
        t = n % (-10) + t
        n = int(n / 10)
    print(t)
