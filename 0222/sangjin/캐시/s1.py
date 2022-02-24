def solution(cacheSize, cities):
    answer = 0
    if cacheSize:
        cache = []
        for city in cities:
            if city.lower() not in cache:
                answer += 5
                if len(cache) == cacheSize:
                    cache.pop(0)
            else:
                answer += 1
                cache.remove(city.lower())
            cache.append(city.lower())
    else:
        answer = 5 * len(cities)

    return answer