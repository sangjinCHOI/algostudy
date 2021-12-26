import sys
sys.stdin = open('input.txt')

for test_case in range(1, int(input())+1):
    N, M = map(int, input().split())
    queue = list(map(int, input().split()))

    for _ in range(M):
        a = queue.pop(0)
        queue.append(a)

    print("#{} {}".format(test_case, queue[0]))