def solution(s):
    stack = []
    for i in s:
        if i == '(' :
            stack.append(i) # '(' 시작
        else:
            if stack == []: # '(' 시작이 아닌 ')' 시작일 떄, 잘못 된 괄호이므로 False
                return False
            else:
                stack.pop() # ')'가 나왔을 떄, 올바른 괄호를 하나씩 짝지어가며 pop
    if stack != []: # list가 비어있지 않다면 즉, '(' 하나 또는 여러개가 남아있는 경우 False
        return False
    return True
