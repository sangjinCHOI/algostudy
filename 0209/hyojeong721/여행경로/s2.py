#통과
def destination(start, tickets, cnt, temp):
    temp.append(start)
    if cnt == len(tickets):
        return

    for i in range(len(tickets)):
        ticket = tickets[i]
        if ticket[0] == start and ticket[-1] != 0:
            ticket.append(0)
            destination(ticket[1], tickets, cnt+1, temp)
            if len(temp) == len(tickets)+1:
                return temp
            else:
                temp.pop()
                cnt -= 1
                ticket.pop(-1)


def solution(tickets):
    tickets.sort(key=lambda x: x[1])
    res = destination('ICN', tickets, 0, temp=[])

    return res

tickets = [["ICN", "AOO"], ["AOO", "BOO"], ["AOO", "COO"], ["COO", "AOO"], ["BOO", "ZOO"]]
returns = ["ICN", "AOO", "COO", "AOO", "BOO", "ZOO"]
#
# tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
# returns = ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]

print(solution(tickets))
