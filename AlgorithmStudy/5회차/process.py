from collections import deque
def solution(priorities, location):
    queue = deque(priorities)
    answer = 0
    while True:
        m = max(queue)  # priorities의 제일 큰 값
        temp = queue.popleft()  # 왼쪽부터 차례대로 수행
        location -= 1   # 수행할 때 마다 위치를 갱신
        #print(answer)
        if not temp == m:   # max값이 아닐 때 마다
            queue.append(temp)  #queue에 max값이 아닌 원소를 다시 추가
            if location < 0 :   #만약 음수값이 max값을 찾기 전에 음수값이 되어버린다면, 마지막 번호를 부여
                location = len(queue) - 1            
        else :
            answer += 1 # location이 음수값이 될 때까지 반복, 원하는 위치에 있는 원소를 찾는 단계
            if location < 0:
                break
    return answer
