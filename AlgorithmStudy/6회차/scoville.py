import heapq
def solution(scoville, K):
    answer = 0
    heap = []           #heap으로 활용 할 배열 생성
    for s in scoville:
        # heap 배열을 힙으로 s원소를 넣어주기
        heapq.heappush(heap, s)
    while True :
        # heap 배열의 최솟값을 꺼내주기
        current = heapq.heappop(heap)
        # 힙이 비어있거나 해당 값이 K보다 작은경우 -> 문제 해결 불가
        if len(heap) < 1 and current < K:
            answer = -1
            break
        if current >= K:
            break
        else:
            answer += 1
            next_s = heapq.heappop(heap)
            heapq.heappush(heap, current + next_s*2)
            
    return answer
