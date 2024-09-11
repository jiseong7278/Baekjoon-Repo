import sys

while True:
    s = sys.stdin.readline().rstrip()

    if s == ".":
        break

    check = True

    stack = []

    for i in range(len(s)):
        if s[i].isalpha():
            continue
        else:
            if s[i] == '(' or s[i] == '[':
                stack.append(s[i])
            elif s[i] == ')':
                if len(stack) > 0:
                    temp = stack.pop()
                    if temp != '(':
                        check = False
                        break
                else:
                    check = False
                    break
            elif s[i] == ']':
                if len(stack) > 0:
                    temp = stack.pop()
                    if temp != '[':
                        check = False
                        break
                else:
                    check = False
                    break

    if len(stack) == 0 and check:
        print("yes")
    else:
        print("no")