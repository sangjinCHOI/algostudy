def solution(number, k):
    stack = [number[0]]

    for n in number[1:]:
        while stack and stack[-1] < n and k > 0:
            stack.pop()
            k -= 1
        stack.append(n)

    if k != 0:
        stack = stack[:-k]

    answer = ""
    for s in stack:
        answer += s

    return answer