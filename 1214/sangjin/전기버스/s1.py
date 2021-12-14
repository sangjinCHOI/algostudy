import sys
sys.stdin = open('input.txt')

for test_case in range(1, int(input())+1):
    K, N, M = map(int, input().split())
    charge = list(map(int, input().split()))

    bus_stop = [0] * (N+1)
    for c in charge:
        bus_stop[c] += 1

    print(bus_stop)
    count = 0
    curr = 0


    while curr < N:
        if curr + K >= N:
            curr = N
        else:
            for k in range(K, 0, -1):
                if bus_stop[curr+k] == 1:
                    curr += k
                    count += 1
                    break
            else:
                count = 0
                break

    print("#{} {}".format(test_case, count))