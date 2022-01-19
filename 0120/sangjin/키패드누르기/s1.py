def distance(curr, target):
    if target == 0:
        target = 11
    if curr == 0:
        curr = 11

    if abs(curr - target) == 0:
        return 0
    elif abs(curr - target) in (1, 3):
        return 1
    elif abs(curr - target) in (2, 4, 6):
        return 2
    elif abs(curr - target) in (5, 7, 9):
        return 3
    else:
        return 4


def solution(numbers, hand):
    answer = ''
    curr_left = 10
    curr_right = 12

    for number in numbers:
        if number in (1, 4, 7):
            answer += 'L'
            curr_left = number
        elif number in (3, 6, 9):
            answer += 'R'
            curr_right = number
        else:
            if distance(curr_left, number) < distance(curr_right, number):
                answer += 'L'
                curr_left = number
            elif distance(curr_left, number) > distance(curr_right, number):
                answer += 'R'
                curr_right = number
            else:
                if hand == 'left':
                    answer += 'L'
                    curr_left = number
                elif hand == 'right':
                    answer += 'R'
                    curr_right = number

    return answer