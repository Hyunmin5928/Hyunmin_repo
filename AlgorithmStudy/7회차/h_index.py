def solution(citations):
    answer = 0
    citations.sort()
    # 오름차순으로 정렬하기
    for index, citation in enumerate(citations):
        # enumerate를 통해서 index번호와 해당 citation값을 추출하여 for문 반복
        if citation >= len(citations) - index :
            # citation값이 해당 citations의 길이 - index번호보다 크거나 같게 되면
            # 원하는 H-Index값을 찾아낸것이다.
            answer = len(citations) - index
            return answer # if문으로 찾으면 바로 return으로 탈출
    return
