def solution(numbers, hand):
    keyboard = {
        1: [0, 0], 2: [0, 1], 3: [0, 2],
        4: [1, 0], 5: [1, 1], 6: [1, 2],
        7: [2, 0], 8: [2, 1], 9: [2, 2],
        '*':[3, 0], 0: [3, 1], '#':[3, 2],
    }
    i = 0
    answer = ''
    L_s = keyboard['*']
    R_s = keyboard['#']
    for num in numbers:
        if num in [1, 4, 7]:
            answer += 'L'
            L_s = keyboard[num]
        elif num in [3, 6, 9]:
            answer += 'R'
            R_s = keyboard[num]
        else:
            left_d = 0
            right_d = 0
            print(L_s, R_s, keyboard[num])
            for a, b, c in zip(L_s, R_s, keyboard[num]):
                left_d += abs(a-c)
                right_d += abs(b-c)

            if left_d > right_d:
                answer += 'R'
                R_s = keyboard[num]
            elif left_d < right_d:
                answer += 'L'
                L_s = keyboard[num]
            else:
                if hand == 'left':
                    answer += 'L'
                    L_s = keyboard[num]
                else:
                    answer += 'R'
                    R_s = keyboard[num]

    return answer

# numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
hand = "right"
print(solution(numbers, hand))

