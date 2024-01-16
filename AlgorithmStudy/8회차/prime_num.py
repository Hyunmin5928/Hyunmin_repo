from itertools import permutations

def prime_num(n) :
    if n < 2 :
        return False
    for i in range(2, n//2 + 1) :
        if n % i == 0 :
            return False
    return True

def solution(numbers):
    answer = 0
    n = []
    ans = []
    for i in range(1, len(numbers) + 1) :
        n.extend(permutations(numbers, i))
        ans = [int(''.join(i)) for i in n]
    ans = set(ans)
    for i in ans:
        if prime_num(i) :
            answer += 1
    return answer
