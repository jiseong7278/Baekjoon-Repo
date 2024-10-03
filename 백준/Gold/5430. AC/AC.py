import sys
from collections import deque

T = int(sys.stdin.readline().rstrip())

answer = []

for _ in range(T):
    command = sys.stdin.readline().rstrip()
    N = int(sys.stdin.readline().rstrip())
    queue = deque(sys.stdin.readline().rstrip()[1:-1].split(","))

    is_reverse = False
    is_error = False

    if N == 0:
        queue = []

    for c in command:
        if c == "R":
            is_reverse = not is_reverse
        else:
            if len(queue) < 1:
                answer.append("error")
                is_error = True
                break
            else:
                if is_reverse:
                    queue.pop()
                else:
                    queue.popleft()

    if not is_error:
        if is_reverse:
            queue.reverse()
        answer.append("[" + ",".join(queue) + "]")

for a in answer:
    print(a)