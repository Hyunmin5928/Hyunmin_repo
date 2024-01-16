import heapq

def solution(jobs):
    answer = 0
    now = 0
    i = 0
    start = -1
    heap = []
    while i < len(jobs):
        for j in jobs:
            # 작업이 요청될 때, 이전 시간과 현재 시간의 조건을 만족하는지 확인 [1,9]는 heap에 들어감
            if start < j[0] <= now:
                # 작업의 소요시간, 작업이 요청시간으로 push
                heapq.heappush(heap, [j[1], j[0]])
        if len(heap) > 0:
            current = heapq.heappop(heap)
            start = now
            now += current[0]            # (더하기) 작업의 소요시간
            answer += (now - current[1]) # (뺴기) 작업의 요청시간
            i += 1
        # 현재 처리할 수 있는 작업이 없으면 현재 시간을 올려줌
        else :
            now += 1
    return int(answer / len(jobs))
