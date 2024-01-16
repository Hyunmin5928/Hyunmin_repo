def solution(brown, yellow):
    total = brown + yellow
    total2 = int(total / 2)
    row, col = 3, 3
    for c in range(3, total2) :
        if total % c == 0 :
            col = c
            row = int(total / col)
            if (row * col) == total :
                if yellow == (row - 2) * (col - 2) :
                    break
    answer = [row, col]
    return answer
