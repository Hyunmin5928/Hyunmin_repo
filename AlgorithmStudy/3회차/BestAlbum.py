from collections import defaultdict
def solution(genres, plays):
    answer = []
    genre_play = defaultdict(dict) 
    total_num = defaultdict(int) 
    for genre,(idx,play) in zip(genres, enumerate(plays)):
        genre_play[genre][idx] = play
        total_num[genre] += play
    #print(genre_play)
    total_num = [key for key, value in sorted(total_num.items(), key=lambda x:x[1], reverse=True)]
    for genre in total_num:
        #print(genre_play)
        answer.extend([key for key, value in sorted(genre_play[genre].items(), key=lambda x:x[1], reverse=True)][:2])
    return answer
