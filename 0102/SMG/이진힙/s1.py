# 힙 배열 최대크기로 먼저 만들어 놓기
# 강의에서 어펜드 쓰면 비효율적이라고 쓰지 말라함
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    nums = [0] + list(map(int, input().split()))
    # 최대크기로 힙 리스트 만들기
    heap = [0]*500
    for i in range(1, N+1):
        # 힙에다 nums 차례로 하나씩 넣기
        heap[i] = nums[i]
        # 들어가서 부모노드랑 비교 후 더 작으면 부모노드와 스왑
        while heap[i] < heap[i//2]:
            heap[i], heap[i//2] = heap[i//2], heap[i]
            i //= 2
    result = 0
    while N > 0:
        # 모든 조상노드 합 구하기
        N //= 2
        result += heap[N]
    print(f'#{tc} {result}')
