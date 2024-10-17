import sys

while True:
    A, B, C = map(int, sys.stdin.readline().rstrip().split())

    if A == 0 and B == 0 and C == 0:
        break

    circle = sorted([A, B, C])

    if circle[0] + circle[1] <= circle[2]:
        print("Invalid")
        continue

    if circle[0] == circle[1] == circle[2]:
        print("Equilateral")
    elif circle[0] == circle[1] or circle[1] == circle[2]:
        print("Isosceles")
    else:
        print("Scalene")