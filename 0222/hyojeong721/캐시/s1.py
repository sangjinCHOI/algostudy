def solution(cacheSize, cities):
    answer = 0
    cache = []
    if cacheSize != 0:
        while cities:
            temp = cities.pop(0).upper()
            if temp in cache:
                if cache:
                    cache.remove(temp)
                cache.append(temp)
                answer += 1
            else:
                if len(cache) == cacheSize:
                    cache.pop(0)
                cache.append(temp)
                answer += 5
    else:
        answer = 5 * len(cities)

    return answer

cacheSize = 5
cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]
print(solution(cacheSize, cities))