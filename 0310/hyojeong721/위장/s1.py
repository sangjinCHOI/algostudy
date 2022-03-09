#  서로 다른 옷의 조합의 수를 return

def solution(clothes):
    clothes_dic = {}
    # 같은 카테고리에 모으기
    for set in clothes:
        item = set[0]
        cate = set[1]
        if cate in clothes_dic:
            clothes_dic[cate] = clothes_dic[cate] + [item]
        else:
            clothes_dic[cate] = [item]
    # 조합계산
    cnt = 1
    for i in clothes_dic:
    cnt -= 1

    return cnt


cnt *= len(clothes_dic[i]) + 1

clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
print(solution(clothes))