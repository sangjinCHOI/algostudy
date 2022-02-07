def transform(curr, target, words, tmp_count):
    global count
    N = len(words)
    M = len(words[0])
    for i in range(N):
        x = 0
        for j in range(M):
            if curr[j] != words[i][j]:
                x += 1

        if x == 1:
            if visited[i] == 0:
                visited[i] = 1
                transform(words[i], target, words, tmp_count + 1)
            else:
                if count > tmp_count:
                    count = tmp_count
                    return
    if tmp_count > count:
        return


count = 999999999999999999999
visited = [0] * 6


def solution(begin, target, words):
    N = len(words)
    M = len(words[0])

    transform(begin, target, words, 0)
    answer = count
    return answer