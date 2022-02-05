def solution(numbers, target):
    answer = 0
    N = len(numbers)
    def dfs(idx, temp):
        nonlocal answer
        if idx != N:
            dfs(idx + 1, temp + numbers[idx])
            dfs(idx + 1, temp - numbers[idx])
        else:
            if temp == target:
                answer += 1
                return
    dfs(0, 0)

    return answer

print(solution([1, 1, 1, 1, 1], 3))