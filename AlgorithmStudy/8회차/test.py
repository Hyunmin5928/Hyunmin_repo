def solution(answers):
    m1 = [1,2,3,4,5]
    m2 = [2,1,2,3,2,4,2,5]
    m3 = [3,3,1,1,2,2,4,4,5,5]
    cnt1 = 0
    cnt2 = 0
    cnt3 = 0
    answer = []
    
    for i in range(len(answers)) :
        s1 = i % 5
        s2 = i % 8
        s3 = i % 10
        if m1[s1] == answers[i] :
            cnt1 += 1
        if m2[s2] == answers[i] :
            cnt2 += 1
        if m3[s3] == answers[i] :
            cnt3 += 1

    m = max(cnt1,cnt2,cnt3)
    
    if m == cnt1:
        answer.append(1)
    if m == cnt2:
        answer.append(2)
    if m == cnt3:
        answer.append(3)
    
    return answer
