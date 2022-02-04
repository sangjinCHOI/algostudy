answer = 0
def DFS(i, value, numbers, target):
    global answer
    N = len(numbers)
    if i == N and target == value:
        answer += 1
        return
    if i == N:
        return

    DFS(i + 1, value - numbers[i], numbers, target)
    DFS(i + 1, value + numbers[i], numbers, target)

def solution(numbers, target):
    DFS(0, 0, numbers, target)
    return answer