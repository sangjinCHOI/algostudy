import copy

Max_score = 0
answers = []

def calcScor(info, myshots):
    enemyScore, myScore = 0, 0
    for i in range(11):
        if (info[i], myshots[i]) == (0, 0):
            continue
        if info[i] >= myshots[i]:
            enemyScore += (10-i)
        else:
            myScore += (10-i)

    return myScore - enemyScore


def dfs(info, myshots, n, i):
    global Max_score, answers
    if i == 11:
        if n != 0:
            myshots[10] = n
        scoreDiff = calcScor(info, myshots)
        if scoreDiff <= 0:
            return
        result = copy.deepcopy(myshots)
        if scoreDiff > Max_score:
            Max_score = scoreDiff
            answers = [result]
            return
        if scoreDiff == Max_score:
            answers.append(result)
        return

    if info[i] < n:
        myshots.append(info[i] + 1)
        dfs(info, myshots, n-info[i]-1, i+1)
        myshots.pop()

    myshots.append(0)
    dfs(info, myshots, n, i+1)
    myshots.pop()


def solution(n, info):
    global Max_score, answers
    dfs(info, [], n, 0)
    if answers == []:
        return -1
    answers.sort(key=lambda x:x[::-1], reverse=True)

    return answers[0]

n = 5
info = [2,1,1,1,0,0,0,0,0,0,0]
print(solution(n, info))