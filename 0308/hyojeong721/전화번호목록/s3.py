import heapq
# heapq 는 첫번째 요소가 최소값이 가지도록 내부적으로 tree 구조형태로 리스트를 재편성한다.
# heappop으로 리스트에서 최소값을 빼오고 나면, 리스트는 나머지 요소들로 min Tree 형태로 재편성된다.
# 그래서 항상 headpop 을 하면 남은 리스트의 첫번째 요소가 최소값이 되게 유지된다.
def solution(pb):
    heapq.heapify(pb)  #  리스트를 min_tree 형태로 재배치한다.
    p = heapq.heappop(pb)
    while pb:
        if p == pb[0][:len(p)]:
            return False
        p = heapq.heappop(pb)
    return True


pb1 = ["119", "97674223", "1195524421"]
print(solution(pb1))
pb2 = ["123","456","789"]
print(solution(pb2))
pb3 = ["12","123","1235","567","88"]
print(solution(pb3))