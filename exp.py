n = int(input())
k = input().split()
num1, num2 = int(k[0]), int(k[1])
yes = num2 / num1
for i in range(n - 1):
    t = input().split()
    n1, n2 = int(t[0]), int(t[1])
    if n2 / n1 - yes > 0.05:
        print("better")
    elif yes - n2 / n1 > 0.05:
        print("worse")
    else:
        print("same")
