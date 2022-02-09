answer = []
cnt = 0
# 테케1번 노패스
def destination(start, tickets, cnt):
    answer.append(start)
    des = ''
    des_idx = 0
    temp_des = ''
    temp_des_idx = 0
    for idx in range(len(tickets)):
        ticket = tickets[idx]
        if ticket[0] == start and ticket[-1] != 0:
            if des == '':
                des = ticket[1]
                des_idx = idx
            else:
                temp_des = ticket[1]
                temp_des_idx = idx

    if temp_des == '':
        tickets[des_idx].append(0)
    else:
        for t in tickets:
            if t[0] == des:
                tickets[des_idx].append(0)
                break
        else:
            des = temp_des
            tickets[temp_des_idx].append(0)

    if cnt == len(tickets):
        return
    else:
        if des != '':
            destination(des, tickets, cnt+1)

def solution(tickets):
    tickets.sort(key=lambda x: x[1])

    destination('ICN', tickets, 0)

    return answer

# print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))
print(solution([["ICN", "AOO"], ["AOO", "BOO"], ["AOO", "COO"], ["COO", "AOO"], ["BOO", "ZOO"]]))
# 답 ["ICN", "AOO", "COO", "AOO", "BOO", "ZOO"]
#
# lst = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
# lst.sort(key=lambda x:x[1])
# print(lst)
# [['ICN', 'ATL'], ['SFO', 'ATL'], ['ATL', 'ICN'], ['ICN', 'SFO'], ['ATL', 'SFO']]
