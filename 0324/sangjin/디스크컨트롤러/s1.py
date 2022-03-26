from heapq import *


def solution(jobs):
    answer = 0
    start, end, count = -1, 0, 0
    hq = []

    while count < len(jobs):
        for job in jobs:
            if start < job[0] <= end:
                heappush(hq, (job[1], job[0]))
        if len(hq) > 0:
            now = heappop(hq)
            start = end
            end += now[0]
            answer += (end - now[1])
            count += 1
        else:
            end += 1
    answer = answer // len(jobs)
    return answer