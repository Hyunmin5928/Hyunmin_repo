def solution(arr):
    stack  = [] #1회용 저장공간의 느낌
    answer = [] #return해줘야 하는 부분
    for i in range(len(arr)):
        if not stack or arr[i] == stack[-1]:   #if not stack의 의미 stack이라는 list에 요소가 있는지 없는지를 확인하는 과정
            stack.append(arr[i])            #위에서의 if문을 바탕으로 arr[i]의 요소를 stack list에 추가
        else:
            answer.append(stack[0])         #stack이 비어있지 않고, arr[i]와 stack list의 마지막 요소가 같지 않은경우에만 stack의 첫                                                 번쨰 요소를 추가
            stack.clear()                   #원하는 값을 answer list에 넣어줬기에 stack list를 초기화
            stack.append(arr[i])            #stack에 새로운 arr[i]요소를 추가
    
    answer.append(stack[0])                 #반복문을 탈출 한 이후의 마지막 요소인 stack[0]을 추가해줌으로서 완료
    return answer
