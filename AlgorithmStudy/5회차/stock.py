from collections import deque
def solution(prices):
    q = deque(prices)
    answer = []
    while len(q) > 0:
        cur_price = q.popleft()
        cnt = 0
        for price in q:
            if price < cur_price :
                cnt += 1
                break
            else :
                cnt += 1
        answer.append(cnt)
    return answer
