from itertools import permutations

def prime(number):
    if number == 1 or number == 0:
        return 0
    for n in range(2, int(number ** 0.5) + 1):
        if number % n == 0:
            return 0
    else:
        return 1

def solution(numbers):
    answer = []

    for i in range(1, len(numbers) + 1):
        for p in set(permutations(numbers, i)):
            tmp = ''
            for x in p:
                tmp += x
            if prime(int(tmp)) and int(tmp) not in answer:
                answer.append(int(tmp))

    return len(answer)