import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    cargo = list(map(int, input().split()))
    truck = list(map(int, input().split()))
    result = 0
    cargo.sort()
    truck.sort()
    print(cargo, truck)
    while cargo:
        if truck and cargo[-1] <= truck[-1]:
            result += cargo.pop()
            truck.pop()
        else:
            cargo.pop()
    print(f'#{tc} {result}')