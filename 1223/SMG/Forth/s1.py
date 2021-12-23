import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    case = list(input().split())
    stack = []
    sign = ['+', '-', '/', '*', '.']
    for i in case:
        if i == '.':
            if len(stack) == 1:
                c = stack.pop()
                print(f'#{tc} {c}')
            else:
                print(f'#{tc} error')
                break
        elif i not in sign:
            stack.append(int(i))
        elif len(stack) < 2:
            print(f'#{tc} error')
            break
        else:
            a = stack.pop()
            b = stack.pop()
            if i == '+':
                stack.append(b+a)
            elif i == '-':
                stack.append(b-a)
            elif i == '*':
                stack.append(b*a)
            else:
                stack.append(b//a)
