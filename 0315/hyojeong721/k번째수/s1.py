
def solution(arr, command):
    answer = []
    for com in command:
        start = com[0]-1
        end = com[1]
        point = com[2]-1
        answer.append(sorted(arr[start:end])[point])

    return answer

arr = [1, 5, 2, 6, 3, 7, 4]
command = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

print(solution(arr, command))