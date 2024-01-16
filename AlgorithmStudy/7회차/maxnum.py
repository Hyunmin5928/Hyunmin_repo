def solution(numbers):
    answer = ''
    numbers = list(map(str, numbers)) # numbers배열을 list(map)을 사용해 str로 변환
    numbers.sort(key=lambda x: x*3, reverse=True)
    # 해당 배열의 숫자들을 이었을때 가장 큰 수가 나오도록 정렬하기
    answer = answer.join(numbers)
    return answer
