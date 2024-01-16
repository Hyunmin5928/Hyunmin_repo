def solution(progresses, speeds):
    answer = []
    num = 0     # 반복 횟수 저장용 숫자
    cnt = 0     # 한 번에 배포되는 작업의 숫자
    while len(progresses) > 0:      # progresses를 지속해서 pop하기 때문에
        if (progresses[0] + num*speeds[0]) >= 100: # 첫번째 요소가 100을 넘기는 시점
            progresses.pop(0)                       
            speeds.pop(0)                          # 각 리스트의 값 pop
            cnt += 1                               # 계속 조건을 만족할 경우, 반복해서 if문을 돌면서 cnt의 값을 증가시킴
        else:
            if cnt > 0:                            # if문을 탈출한 이후 cnt의 값이 0이 아닌 양수일 때 answer에 값을 넣어줌
                answer.append(cnt)
                cnt = 0                            # 초기화
            num += 1                               # 반복 횟수를 else문에서 증가시킴. if문은 확인 and cnt의 값을 증가시키는 부분
    answer.append(cnt)                             # while문을 탈출하면서 생긴 마지막 값을 넣어주는 부분
    return answer       
