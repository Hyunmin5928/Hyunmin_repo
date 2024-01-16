import itertools
def solution(k, dungeons):
    n = len(dungeons)
    nDr = list(itertools.permutations(dungeons, n))
    n1 = k
    Mnum = 0
    cnt = 0
    #print(list(nDr))
    for i in nDr :
        #print(i)
        for F,D in i :
            if k >= F:
                cnt = cnt + 1
                k = k - D
                #print(cnt)
        k = n1
        if Mnum < cnt :
            Mnum = cnt
        cnt = 0
    answer = Mnum
    return answer
