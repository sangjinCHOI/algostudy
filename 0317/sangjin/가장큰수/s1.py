def solution(numbers):
    numbers = list(map(str, numbers))
    numbers = sorted(numbers, key = lambda x: x*3, reverse=True)

    answer = ''
    for i in range(len(numbers)):
        answer += str(numbers[i])
    return answer