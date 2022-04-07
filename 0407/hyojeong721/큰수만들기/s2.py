def solution(number, k):
    stack=[]
    numbers = list(map(int, number))

    for num in numbers:
        while stack and k > 0 and stack[-1] < num:
            stack.pop()
            k -= 1
        stack.append(num)

    while k and stack:
        stack.pop()
        k -= 1
    answer = ''.join(list(map(str,stack)))
    return answer

print(solution("4177252841", 4))