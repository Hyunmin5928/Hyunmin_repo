import heapq
def solution(operations):
    answer = []
    heap = []
    for opr in operations:
        # 연산자와 숫자를 split
        f, n = opr.split()
        n = int(n)
        # I 연산자의 경우 -> 해당 숫자 삽입
        if f == 'I':
            heapq.heappush(heap, n)
        # D 연산자, 1인 경우 -> 최댓값 삭제
        elif f == 'D' and n == 1:
            if len(heap) != 0:
                max_n = max(heap)
                heap.remove(max_n)
        # D 연산자, -1인 경우 -> 최솟값 삭제
        else:
            if len(heap) != 0:
                heapq.heappop(heap)
    if len(heap) == 0:
        answer = [0,0]
    else:
        answer = [max(heap), heapq.heappop(heap)]
    return answer
