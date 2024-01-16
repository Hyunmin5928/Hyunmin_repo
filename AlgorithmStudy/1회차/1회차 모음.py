##평균 구하기
def solution(arr):
    answer = sum(arr)/len(arr)
    return answer

##짝수와 홀수
def solution(num):
    ans = ''
    if (num%2) == 0 :
        ans = "Even"
    elif (num%2) == 1:
        ans = "Odd"
    answer = ans
    return answer

##약수의 합
def solution(n):
    ans = []
    i = 1
    while i <= n:
        if (n%i) == 0:
            ans.append(i)
        i += 1
    answer = sum(ans)
    return answer

##자릿수 더하기
def solution(n):
    ans = 0
    while n > 0 :
        ans += n%10
        n //= 10 
    answer = ans
    return answer

##x만큼 간격이 있는 n개의 숫자
def solution(x, n):
    ans = []
    num = x
    while n > 0 :
        ans.append(x)
        x += num
        n -= 1
    answer = ans
    return answer

## 문자열 내 p와 y의 개수
def solution(s):
    s = s.lower()
    return s.count('p') == s.count('y')

#나머지가 1이 되는 수 찾기
def solution(n):
    ans = 0
    a = 1
    while True:
        if (n % a) == 1 :
            ans = a
            break
        a += 1
    print (ans)
    answer = ans
    return answer
