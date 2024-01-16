from collections import Counter
def solution(participant, completion):
    ans = Counter(participant) - Counter(completion)
    print(ans)
    print(list(ans.keys())[0])
    return list(ans.keys())[0]
#     hash = {}
#     for i in participant:
#         if i in hash:
#             hash[i] += 1
#         else:
#             hash[i] = 1
#     for i in completion:
#         if hash[i] == 1:
#             del hash[i]
#         else:
#             hash[i] -= 1
#     print(hash)
#     answer = list(hash.keys())[0]
#     return answer

#     # participant.sort()
    # completion.sort()
    # i = 0
    # while i < len(completion):
    #     if participant[i] != completion[i]:
    #         break
    #     i += 1
    # print(participant[i])
    # answer = participant[i]
    # return answer
