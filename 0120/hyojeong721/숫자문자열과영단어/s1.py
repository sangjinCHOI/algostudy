def solution(s):
    numbers = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
    }
    i = 0
    en = list(numbers.keys())
    num = list(numbers.values())
    temp = ''
    answer = ''
    while i < len(s):
        temp += s[i]
        if temp in en:
            answer += numbers[temp]
            temp = ''
        elif temp in num:
            answer += temp
            temp = ''
        i += 1

    return int(answer)


# s = "one4seveneight"
# s = "23four5six7"
s = "2three45sixseven"
# s = '123'
print(solution(s))

