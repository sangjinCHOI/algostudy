import sys
sys.stdin = open('input.txt')

T = int(input())

def search(stack):
    global case
    for i in case:
        if i == '{' or i == '}' or i == '(' or i == ')':
            if not stack:
                stack.append(i)
            elif i == '}':
                if stack[-1] == '{':
                    stack.pop()
                else:
                    return 0
            elif i == ')':
                if stack[-1] == '(':
                    stack.pop()
                else:
                    return 0
            else:
                stack.append(i)
    if stack:
        return 0
    else:
        return 1
for tc in range(1, T+1):
    case = input()
    result = search([])
    print(f'#{tc} {result}')