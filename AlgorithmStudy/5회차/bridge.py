from collections import deque
def solution(bridge_length, weight, truck_weights):
    q = deque(truck_weights)
    cnt = 0
    b_w = 0
    bridge = [0]*bridge_length
    while bridge :
        cnt += 1
        b_w -= bridge.pop(0)
        if q:
            if  b_w + q[0] <= weight:
                temp = q.popleft()
                bridge.append(temp)
                b_w += temp
            else :
                bridge.append(0)
    return cnt
