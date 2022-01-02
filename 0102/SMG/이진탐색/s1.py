# 중위순회
# 이진트리의 배열 저장 => 배열의 길이는 2**(n+1)-1 (n은 레벨) (연결리스트 표현이 더 효율적)
# 노드 번호가 i인 노드의 부모 노드 번호 => i//2
# 노드 번호가 i인 노드의 왼쪽 자식 노드 번호 => 2*i
# 노드 번호가 i인 노드의 오른쪽 자식 노드 번호 => 2*i+1

import sys
sys.stdin = open('input.txt')

T = int(input())

def in_order(n):
    global cnt
    if n <= N:
        in_order(n*2)
        tree[n] = cnt
        cnt += 1
        in_order(n*2+1)

for tc in range(1, T+1):
    N = int(input())
    tree = [0]*(N+1)
    cnt = 1
    in_order(1)
    print(f'#{tc} {tree[1]} {tree[N//2]}')
