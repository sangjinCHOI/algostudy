from collections import deque

def solution(p, location):
    answer = 0
    p = deque(p)
    index = deque([i for i in range(len(p))])

    while p:
        num = p.popleft()
        idx = index.popleft()
        c = 0
        for i in range(len(p)):
            if p[i] > num:
                c=1
        if c==0:
            answer += 1
            if idx == location:
                return answer
        else:
            p.append(num)
            index.append(idx)



    return answer
print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))
