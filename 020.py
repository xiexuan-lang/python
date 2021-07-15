import math

s = input().split()
a, b, c = eval(s[0]), eval(s[1]), eval(s[2])
if b * b == 4 * a * c:
    print("x1=x2={:.5f}".format(((-b + math.sqrt(b * b - 4 * a * c)) / (2 * a))))
if b * b > 4 * a * c:
    print("x1={:.5f};x2={:.5f}".format(((-b + math.sqrt(b * b - 4 * a * c)) / (2 * a)),
                                       ((-b - math.sqrt(b * b - 4 * a * c)) / (2 * a))))
if b * b < 4 * a * c:
    print("x1={:.5f}+{:.5f}i;x2={:.5f}{:.5f}i".format((-b / (2 * a)), (math.sqrt(4 * a * c - b * b) / (2 * a)),
                                                     (-b / (2 * a)), (-math.sqrt(4 * a * c - b * b) / (2 * a))))
