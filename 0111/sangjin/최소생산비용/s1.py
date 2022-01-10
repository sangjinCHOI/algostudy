import sys
sys.stdin = open('input.txt')

def calculate(product, cost):
    global  result
    if product == N and cost < result:
        result = cost
        return

    if cost >= result:
        return

    for factory in range(N):
        if not visited[factory]:
            visited[factory] = 1
            calculate(product+1, cost+V[product][factory])
            visited[factory] = 0


for test_case in range(1, int(input())+1):
    N = int(input())
    V = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    result = 999999999

    calculate(0, 0)

    print("#{} {}".format(test_case, result))

