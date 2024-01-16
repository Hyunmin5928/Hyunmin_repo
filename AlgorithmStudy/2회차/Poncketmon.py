from collections import Counter
def solution(nums):
    len1 = len(nums)
    num1 = Counter(nums)
    len2 = len(Counter(nums))
    print(nums)
    print(num1)
    if len2 >= (len1/2):
        len2 = (len1/2)
    answer = len2
    return answer
