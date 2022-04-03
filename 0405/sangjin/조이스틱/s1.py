def solution(name):
    answer = 0
    shift = len(name) - 1

    for i, char in enumerate(name):
        answer += min(ord(char) - 65, 91 - ord(char))

        if char == 'A':
            target = i
            while target < len(name) and name[target] == 'A':
                target += 1
            if i == 0:
                left = 0
            else:
                left = i - 1

            right = len(name) - target
            shift = min(shift, left + right + min(left, right))

    answer += shift
    return answer