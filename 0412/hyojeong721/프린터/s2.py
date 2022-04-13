from collections import deque

def solution(p, location):
    answer = 1
    p = deque(p)
    index = deque([i for i in range(len(p))])

    while p:
        num = p.popleft()
        idx = index.popleft()
        if num < max(p):
            p.append(num)
            index.append(idx)
        else:
            if idx == location:
                return answer
            answer += 1

    return answer

print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))
