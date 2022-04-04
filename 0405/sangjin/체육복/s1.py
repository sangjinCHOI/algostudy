def solution(n, lost, reserve):
    extra = []
    miss_a = []
    miss_b = []
    for r in reserve:
        if r not in lost:
            extra.append(r)
    for l in lost:
        if l not in reserve:
            miss_a.append(l)
            miss_b.append(l)

    for e in extra:
        if e + 1 in miss_a:
            miss_a.remove(e + 1)
        elif e - 1 in miss_a:
            miss_a.remove(e - 1)

    for e in extra:
        if e - 1 in miss_b:
            miss_b.remove(e - 1)
        elif e + 1 in miss_b:
            miss_b.remove(e + 1)

    a = n - len(miss_a)
    b = n - len(miss_b)

    return max(a, b)