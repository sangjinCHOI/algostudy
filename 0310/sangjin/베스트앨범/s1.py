def solution(genres, plays):
    answer = []
    best = {}
    total = {}
    for i, [genre, play] in enumerate(zip(genres, plays)):
        if genre in best:
            best[genre].append((i, play))
            total[genre] += play
        else:
            best[genre] = [(i, play)]
            total[genre] = play

    best_genres = sorted(total.items(), key=lambda x: x[1], reverse=True)

    for bg in best_genres:
        tmp = sorted(best[bg[0]], key=lambda x: x[1], reverse=True)
        for i in range(len(tmp)):
            answer.append(tmp[i][0])
            if i == 1:
                break

    return answer