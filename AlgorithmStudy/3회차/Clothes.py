from collections import defaultdict

def solution(clothes):
    clothes_list = defaultdict(int)
    answer = 1
    for i in range(len(clothes)):
        clothes_list[clothes[i][1]] += 1
    for clothes_value in clothes_list.values():
        answer *= (1 + clothes_value)
    return answer - 1
