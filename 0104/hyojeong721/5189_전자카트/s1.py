import sys
import itertools
sys.stdin = open('input.txt')

# 사무실에서 출발해 각 구역을 한 번씩만 방문하고
# 사무실로 돌아올 때의 최소 배터리 사용량 구하기
# 1번 사무실 N번 관리구역 번호(3<=N<=10) / 배터리양(<=100)

def usage(temp_sum):
    global res
    section = [i for i in range(2, N+1)]
    turn = list(itertools.permutations(section))
    print(turn)

    for temp_turn in turn:
        temp_sum = battery[1][temp_turn[0]]

        for i in range(len(temp_turn)):
            if i != len(temp_turn)-1:
                temp_sum += battery[temp_turn[i]][temp_turn[i+1]]
        temp_sum += battery[temp_turn[-1]][1]

        if temp_sum < res:
            res = temp_sum

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    battery =[[0]*(N+1)] + [[0] + list(map(int, input().split())) for _ in range(N)]
    res = 100 * N + 100 * (N-1)

    usage(0)
    print("#{} {}".format(tc, res))