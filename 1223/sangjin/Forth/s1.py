import sys
sys.stdin = open('input.txt')

for test_case in range(1, int(input())+1):
    formula = list(input().split())
    stack = []

    for element in formula:
        if element.isdigit():
            stack.append(int(element))
        elif element == '.':
            if len(stack) == 1:
                result = stack.pop()
            else:
                result = 'error'
        else:
            if len(stack) < 2:
                result = 'error'
                break
            else:
                y = stack.pop()
                x = stack.pop()
                if element == '+':
                    stack.append(x+y)
                elif element == '-':
                    stack.append(x-y)
                elif element == '*':
                    stack.append(x*y)
                elif element == '/':
                    stack.append(x//y)

    print("#{} {}".format(test_case, result))

