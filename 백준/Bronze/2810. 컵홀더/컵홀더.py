import sys

N = int(sys.stdin.readline().rstrip())

seats = sys.stdin.readline().rstrip()

if N == seats.count("S"):
    print(N)
else:
    seats = seats.replace("LL", "S")
    print(seats.count("S") + 1)