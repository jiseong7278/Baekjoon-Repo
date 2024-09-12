import sys

N = int(sys.stdin.readline().rstrip())

person = []

for i in range(N):
    age, name = sys.stdin.readline().rstrip().split()
    age = int(age)
    person.append([age, name, i])

person.sort(key=lambda x: (x[0], x[2]))

for p in person:
    print(p[0], p[1])