def check_prime(n):
    check = 1
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                check = 0
                break
        return check


def solution(n, k):
    num_n = ''
    while n:
        n, tmp = divmod(n, k)
        num_n += str(tmp)
    num_n = num_n[::-1]

    prime = []
    li = num_n.split('0')
    for i in li:
        if i:
            prime.append(int(i))

    count = 0
    for p in prime:
        if check_prime(p):
            count += 1

    return count