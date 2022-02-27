def solution(n, t, m, p):
    answer = '0'
    length = 1

    for number in range(1, t * m):
        num_n = ''
        while number:
            tmp = str(number % n)
            if len(tmp) > 1:
                tmp = chr(int(tmp) + 55)
            num_n += tmp
            number //= n

        num_n = num_n[::-1]
        length += len(num_n)
        answer += num_n

        if length > t * m:
            break

    answer = answer[p - 1:len(answer):m][:t]
    return answer