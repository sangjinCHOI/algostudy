# TIL 12/14

### for - else문

: for문이 break 등으로 중간에 빠져나오지 않고 끝까지 실행 됐을 경우, else문이 실행되는 방식



- 4831_전기버스 예시

```python
t = int(input())

for tc in range(1, t+1):
    k, n, m = map(int, input().split())
    charge = list(map(int, input().split()))

    cnt = 0
    now = 0

    while now + k < n:
        temp = now + k
        
        for i in range(k):
            if temp in charge:
                now = temp
                cnt += 1
                break
            else:
                temp -= 1
        else:
            cnt = 0
            break

    print('#{} {}'.format(tc, cnt))




```

