answer = 9999999
# test3만 걸림 => hhf->hih 인 경우도 17번줄에서 통과하기때문에 걸림
def dfs(temp, target, words, cnt, visited):
    global answer
    if temp in visited:
        return
    else:
        visited.append(temp)
        cnt += 1

    for c in words:
        temp_temp2 = c
        if c in visited:
            continue
        for t in temp:
            temp_temp2 = temp_temp2.replace(t, '')
        if len(temp_temp2) == 1:
            temp2 = c
            if temp2 == target:
                if answer > cnt:
                    answer = cnt
            else:
                dfs(temp2, target, words, cnt, visited)

def solution(begin, target, words):
    cnt = 0
    visited = []
    if target not in words:
        return 0

    dfs(begin, target, words, cnt, visited)

    return answer

print(solution('hit', 'cog', ["hot", "dot", "dog", "lot", "log", "cog"]))
# print(solution('hit', 'cog', ["hot", "dot", "dog", "lot", "log"]))