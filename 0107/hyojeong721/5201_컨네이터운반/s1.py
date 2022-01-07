import sys
sys.stdin = open('input.txt')


def container_out(truck):
    global total

    while truck:
        if truck in W:
            total += truck
            W.remove(truck)
            break
        else:
            truck -= 1

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    W = list(map(int, input().split()))
    T = list(map(int, input().split()))
    total = 0

    for m in range(M):
        container_out(T[m])
    print("#{} {}".format(tc, total))

