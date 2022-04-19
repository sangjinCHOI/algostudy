def solution(prices):
    answer = []
    size = len(prices)
    for idx, now in enumerate(prices):
        cnt = 0
        for i in range(idx+1, size):
            if prices[i] >= now:
                cnt += 1
            else:
                cnt += 1
                break
        answer.append(cnt)
    return answer

print(solution([1, 2, 3, 2, 3])) #[4, 3, 1, 1, 0]
print(solution([1, 2, 3, 2, 3, 3, 1])) #[6, 5, 1, 3, 2, 1, 0]
