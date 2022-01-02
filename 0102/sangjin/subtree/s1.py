import sys
sys.stdin = open('input.txt')

for test_case in range(1, int(input())+1):
    E, N = map(int, input().split())
    lines = list(map(int, input().split()))
    result = [N]
    stack = [N]

    while stack:
        x = stack.pop()
        for i in range(0, 2*E, 2):
            if lines[i] == x:
                stack.append(lines[i+1])
                result.append(lines[i+1])

    print("#{} {}".format(test_case, len(result)))

