import sys

N = sys.stdin.readline().rstrip()

if N[-1:] == "0":
    print(int(N[-2:]) + int(N[:-2]))
else:
    print(int(N[-1:]) + int(N[:-1]))