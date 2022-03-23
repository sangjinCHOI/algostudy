import heapq


def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0

    if min(scoville) >= K:
        return 0

    while (len(scoville) > 1):
        small = heapq.heappop(scoville)
        if small >= K:
            break
        big = heapq.heappop(scoville)
        heapq.heappush(scoville, small + (big) * 2)
        answer += 1

    if min(scoville) < K:
        return -1

    return answer