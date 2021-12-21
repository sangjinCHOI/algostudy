import sys
sys.stdin = open('input.txt')

for test_case in range(1, int(input())+1):
    N = int(input())
    matrix = [[0] * 10 for _ in range(10)]

    for _ in range(N):
        r1, c1, r2, c2, color = map(int, input().split())

        for i in range(r1, r2+1):
            for j in range(c1, c2+1):
                matrix[i][j] += color

        cnt = 0
        for r in range(10):
            for c in range(10):
                if matrix[r][c] == 3:
                    cnt += 1

    print("#{} {}".format(test_case, cnt))