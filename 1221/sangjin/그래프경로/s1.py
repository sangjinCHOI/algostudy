import sys
sys.stdin = open('input.txt')

def dfs(S, G):
    stack = [S]
    visited = [S]

    while stack:
        for line in lines:
            # 길이 있고 다음 지점을 방문 안 했으면 방문
            if line[0] == S and line[1] not in visited:
                    S = line[1]
                    stack.append(S)
                    visited.append(S)
                    break
        # 갈 수 있는 곳이 없으면 뒤로
        else:
            stack.pop()
            if stack:
                S = stack[-1]
        if S == G:
            return 1
    return 0




for test_case in range(1, int(input())+1):
    V, E = map(int, input().split())
    lines = []
    for _ in range(E):
        lines.append(list(map(int, input().split())))
    S, G = map(int, input().split())

    print("#{} {}".format(test_case, dfs(S, G)))