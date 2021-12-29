import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    code = input().split()
    stack = [int(code.pop(0))]

    sign = ['+', '-', '*', '/']
    while stack:
        temp = code.pop(0)
        if temp not in sign:
            if temp == '.' and len(stack) == 1:
                print("#{}".format(tc), stack.pop())
                break
            elif temp == '.' and len(stack) > 1:
                print("#{} error".format(tc))
                break
            else:
                stack.append(int(temp))
        else:
            if len(stack) >= 2:
                two = stack.pop()
                one = stack.pop()
                if temp == '+':
                    stack.append(one+two)
                elif temp == '-':
                    stack.append(one-two)
                elif temp == '*':
                    stack.append(one*two)
                elif temp == '/':
                    stack.append(one//two)
            else:
                print("#{} error".format(tc))
                break

