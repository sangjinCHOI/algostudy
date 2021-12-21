import sys
sys.stdin = open('input.txt')

def check(arr):
    stack = []
    sign_open = ['(', '{']
    sign_close = [')', '}']
    print(arr)
    for c in arr:
        if c in sign_open:
            stack.append(c)
        if c in sign_close:
            if stack:
                temp = stack.pop()
                if c == '}' and temp == '(':
                    return 0
                if c == ')' and temp == '{':
                    return 0
            else:
                return 0
    if stack:
        return 0
    else:
        return 1

T = int(input())
for tc in range(1, T+1):
    sentence = list(input())
    res = check(sentence)
    print('#{} {}'.format(tc, res))