def transform(begin, target, words, visited):
    count = 0
    stack = [(begin, count)]

    while stack:
        curr, cnt = stack.pop()
        if curr == target:
            return cnt

        for i in range(len(words)):
            if visited[i]:
                continue
            tmp = 0
            for j in range(len(words[0])):
                if curr[j] != words[i][j]:
                    tmp += 1
            if tmp == 1:
                visited[i] = 1
                stack.append((words[i], cnt + 1))


def solution(begin, target, words):
    answer = 0
    if target not in words:
        return answer

    N = len(words)
    visited = [0] * N

    answer = transform(begin, target, words, visited)
    return answer