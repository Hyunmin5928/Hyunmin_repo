from selenium import webdriver
import time
from bs4 import BeautifulSoup as bs
import pandas as pd 
from collections import OrderedDict

# case를 지정하여 원하는 차트를 선택해서 다운로드
print("원하는 차트를 선택하세요 ")
case = input("1 : TOP100 \n2 : 일간차트 \n3 : 주간차트 \n4 : 월간차트 \n5 : POP \n6 : J-POP\n")

url = 'https://www.melon.com/'
driver = webdriver.Chrome('/Users/hunmi/Downloads/chromedriver_win32/chromedriver')
driver.implicitly_wait(10)      # 해당 url에 접속하고 driver가 실행되는 시간을 벌어주는 함수, 오류가 일어나지 않게 해줄 수 있음.
driver.get(url)

if case == '1': # Top 100
    csv_path = 'Top100Chart.csv'    # 실행 파일 위치에 해당 이름으로 저장
    driver.find_element_by_xpath('//*[@id="gnb_menu"]/ul[1]/li[1]/a/span[2]').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="gnb_menu"]/ul[1]/li[1]/div/ul/li[1]/a/span').click()
    time.sleep(2)

elif case == '2': # 일간
    csv_path = 'Today100Chart.csv'
    driver.find_element_by_xpath('//*[@id="gnb_menu"]/ul[1]/li[1]/a/span[2]').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="gnb_menu"]/ul[1]/li[1]/div/ul/li[2]/a/span').click()
    time.sleep(2)
    
elif case == '3': # 주간
    csv_path = 'Week100Chart.csv'
    driver.find_element_by_xpath('//*[@id="gnb_menu"]/ul[1]/li[1]/a/span[2]').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="gnb_menu"]/ul[1]/li[1]/div/ul/li[3]/a/span').click()
    time.sleep(2)
    
elif case == '4': # 월간
    csv_path = 'Month100Chart.csv'
    driver.find_element_by_xpath('//*[@id="gnb_menu"]/ul[1]/li[1]/a/span[2]').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="gnb_menu"]/ul[1]/li[1]/div/ul/li[4]/a/span').click()
    time.sleep(2)
    
elif case == '5': # POP
    csv_path = 'POP50Chart.csv'
    driver.find_element_by_xpath('//*[@id="gnb_menu"]/ul[1]/li[3]/a/span[2]').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="gnb_menu"]/ul[1]/li[3]/div/ul/li[2]/a/span').click()
    time.sleep(2)
    
elif case == '6': # J-POP
    csv_path = 'J-POP50Chart.csv'
    driver.find_element_by_xpath('//*[@id="gnb_menu"]/ul[1]/li[3]/a/span[2]').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="gnb_menu"]/ul[1]/li[3]/div/ul/li[3]/a/span').click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="conts"]/div[2]/ul/li[5]/a/span').click()
    time.sleep(2)

#//*[@id="gnb_menu"]/ul[1]/li[1]/a/span[2] 멜론차트
#//*[@id="gnb_menu"]/ul[1]/li[1]/div/ul/li[1]/a/span @@ top100페이지
#//*[@id="gnb_menu"]/ul[1]/li[1]/div/ul/li[2]/a/span @@ 일간페이지
#//*[@id="gnb_menu"]/ul[1]/li[1]/div/ul/li[3]/a/span @@ 주간
#//*[@id="gnb_menu"]/ul[1]/li[1]/div/ul/li[4]/a/span @@ 월
#//*[@id="gnb_menu"]/ul[1]/li[2]/a/span[2] 최신음악
#//*[@id="gnb_menu"]/ul[1]/li[3]/a/span[2] 장르음악
#//*[@id="gnb_menu"]/ul[1]/li[3]/div/ul/li[2]/a/span 장르음악 해외 pop 50번
#//*[@id="gnb_menu"]/ul[1]/li[3]/div/ul/li[3]/a/span 장르음악 그외인기장르
#//*[@id="conts"]/div[2]/ul/li[5]/a/span j-pop 50번

chart = driver.page_source
soup = bs(chart, 'html.parser')
chart_soup = soup.select('tbody > tr')

song_list = []

for song in chart_soup:
    rank = song.find('span', class_= 'rank').get_text()
    title = song.find('div', class_= 'ellipsis rank01').get_text()
    #song_artist = song.find('div', class_= 'ellipsis rank02').get_text()
    artist = song.find('span', class_= 'checkEllipsis').get_text()
    album = song.find('div', class_= 'ellipsis rank03').get_text()
    likes = song.find('button', class_ = 'button_etc like').get_text()
    # text상태로 가져온 요소들을 list에 append해줌 필요없는 문자는 제거
    song_list.append([rank, title.replace('\n', ''), artist.replace('\n', ''), album.replace('\n', ''), likes.replace('\n', '').replace('좋아요총건수', '')])

# 드라이버 종료
driver.quit()

# List를 Dataframe으로 변환
df = pd.DataFrame(song_list, columns = ['Rank', 'Title', 'Artist', 'Album', 'Likes count'])

# Dataframe을 csv파일로 저장 한글이 encoding되기 위해서 utf-8-sig방식을 사용
df.to_csv(csv_path, index=False, encoding='utf-8-sig')

