import sys

a, b, c, d, e, f = map(int, sys.stdin.readline().rstrip().split())
y = (c*d - a*f)//(d*b - a*e)
x = (c*e - b*f)//(a*e - b*d)
print(x, y)