def solution(array, commands):
    answer = []
    for n in range(len(commands)):
        i = commands[n][0]
        j = commands[n][1]
        k = commands[n][2]
        arr = sorted(array[i - 1:j])

        tmp = arr[k - 1]
        answer.append(tmp)

    return answer