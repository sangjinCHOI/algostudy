answer = 9999999
visited = []
# 통과
def dfs(temp, target, words, cnt):
    global answer, visited
    if temp in visited:
        return
    else:
        visited.append(temp)
        cnt += 1

    for c in words:
        temp2 = c
        temp_cnt = 0
        for i in range(len(temp)):
            if temp2[i] == temp[i]:
                temp_cnt += 1

        if temp_cnt == len(temp)-1:
            if temp2 == target:
                answer = cnt
            else:
                # 이미 나와잇는 최소과정보다 더 적은 경우만 탐색
                if answer > cnt:
                    dfs(temp2, target, words, cnt)
    visited.pop()

def solution(begin, target, words):
    cnt = 0
    if target not in words:
        return 0

    dfs(begin, target, words, cnt)

    return answer

print(solution('hit', 'cog', ["hot", "dot", "dog", "lot", "log", "cog"]))
# print(solution('hit', 'cog', ["hot", "dot", "dog", "lot", "log"]))