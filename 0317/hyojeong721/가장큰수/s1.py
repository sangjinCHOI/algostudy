def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x * 3, reverse=True)  # 문제에서 원소는 1000이하라고 해서
    print(numbers)
    return str(int(''.join(numbers))) # [0,0,0]을 처리해주기 위해 int바꿨다가 str로 바꿈(tc11번 걸림)

numbers = [0,0,0]
print(solution(numbers))