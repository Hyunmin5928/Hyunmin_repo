def solution(sizes):
    w = []
    h = []
    for size in sizes :
        w.append(max(size))
        h.append(min(size))
    answer = max(w) * max(h)
    return answer
