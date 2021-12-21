import sys
sys.stdin = open('input.txt')

for test_case in range(1, int(input())+1):
    text = list(input())
    stack = []

    for t in text:
        if t == "{":
            stack.append(t)
        elif t == "(":
            stack.append(t)
        elif t == "}":
            if stack:
                if stack[-1] == "{":
                    stack.pop()
                else:
                    stack.append(t)
            else:
                stack.append(t)
        elif t == ")":
            if stack:
                if stack[-1] == "(":
                    stack.pop()
                else:
                    stack.append(t)
            else:
                stack.append(t)

    if not stack:
        result = 1
    else:
        result = 0

    print("#{} {}".format(test_case, result))