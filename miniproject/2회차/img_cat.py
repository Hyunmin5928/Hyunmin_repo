#step1.관련 패키지 import
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup as bs
from urllib.request import urlretrieve
import os

#step2.검색할 키워드 입력
query = input('검색할 키워드를 입력하세요: ')

#step3.크롬드라이버로 원하는 url로 접속
url = 'https://www.naver.com/'
driver = webdriver.Chrome('/Users/hunmi/Downloads/chromedriver_win32/chromedriver')
driver.get(url)
time.sleep(3)

#step4.검색창에 키워드 입력 후 엔터
search_box = driver.find_element_by_css_selector("input#query")
search_box.send_keys(query)
search_box.send_keys(Keys.RETURN)
time.sleep(3)

#step5.이미지 탭 클릭
driver.find_element_by_xpath('//*[@id="lnb"]/div[1]/div/ul/li[2]/a').click()
time.sleep(2)

#step6.이미지 추출
img_thumbnail = driver.find_elements_by_css_selector("img._image._listImage")
link_thumbnail = []
for img in img_thumbnail:
    link_thumbnail.append(img.get_attribute('src'))

# 이미지 저장할 폴더 생성
# path_folder의 경로는 각자 저장할 폴더의 경로를 적어줄 것(ex.img_download)
path_folder = '/Users/hunmi/Downloads/img_download/'
if not os.path.isdir(path_folder):
    os.mkdir(path_folder)

# 이미지 다운로드
i = 0
for link in link_thumbnail:          
    i += 1
    urlretrieve(link, path_folder+query+ f'{i}.jpg') #link에서 이미지 다운로드, './imgs/'에 파일명은 index와 확장자명으로
    if i >= 10:
        break
