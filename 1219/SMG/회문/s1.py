import sys
sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T+1):
    N, M = map(int, input().split())
    mat = [input() for _ in range(N)]
    for i in range(N):
        for j in range(N-M+1):
            # 가로 검사
            if mat[i][j:j+M] == mat[i][j:j+M][::-1]:
                print(f'#{tc} {mat[i][j:j+M]}')
                break
            # 세로 검사
            temp = ''
            for a in range(M):
                temp += mat[j+a][i]
            if temp == temp[::-1]:
                print(f'#{tc} {temp}')
                break

