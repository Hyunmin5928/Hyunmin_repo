from itertools import product
def solution(word):
    wordlist = ['A', 'E', 'I', 'O', 'U']
    words = []
    for i in range(1, 6):
        prod = list(product(wordlist, repeat = i))
        for w in prod:
            words.append(''.join(w))
        #print(prod)
        #print(words)
    #print(words)
    words.sort()
    #print(words)
    answer = words.index(word) + 1
    return answer
