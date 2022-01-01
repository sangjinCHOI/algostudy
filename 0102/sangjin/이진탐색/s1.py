import sys
sys.stdin = open('input.txt')

def inorder(n):
    global num
    if n <= N:
        inorder(n*2)
        tree[n] = num
        num += 1
        inorder(n*2 + 1)

for test_case in range(1, int(input())+1):
    N = int(input())
    tree = [0 for _ in range(N+1)]
    num = 1
    inorder(1)
    print("#{} {} {}".format(test_case, tree[1], tree[N//2]))