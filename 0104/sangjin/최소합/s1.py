import sys
sys.stdin = open('input.txt')

for test_case in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if i == 0 and j > 0:
                arr[i][j] += arr[i][j-1]
            elif i > 0 and j == 0:
                arr[i][j] += arr[i-1][j]
            elif i > 0 and j > 0:
                arr[i][j] += min(arr[i-1][j], arr[i][j-1])

    print("#{} {}".format(test_case, arr[N-1][N-1]))