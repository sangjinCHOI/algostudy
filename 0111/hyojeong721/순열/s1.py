
def permutation(order, k, n):
    if k == n:
        print(order)
    else:
        check = [False] * n
        for i in range(k):
            check[order[i]] = True

        for i in range(n):
            if check[i] == False:
                order[k] = i
                permutation(order, k+1, n)

order = [0] * 4
permutation(order, 0, 4)