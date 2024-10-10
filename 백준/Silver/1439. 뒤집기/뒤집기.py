import sys

S = sys.stdin.readline().rstrip()

cur_digit = "-1"

zero = 0
one = 0

for s in S:
    if s == "0" and s is not cur_digit:
        zero += 1
        cur_digit = s
    elif s == "1" and s is not cur_digit:
        one += 1
        cur_digit = s

print(min(zero, one))