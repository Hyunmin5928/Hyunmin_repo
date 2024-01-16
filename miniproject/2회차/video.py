#step1.관련 패키지 import
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from urllib.request import urlretrieve
import os
import time

#step2.검색할 키워드 입력
query = input('검색할 키워드를 입력하세요: ')

#step3.크롬드라이버로 원하는 url로 접속
url = 'https://www.google.com/'
driver = webdriver.Chrome('/Users/hunmi/Downloads/chromedriver_win32/chromedriver')
driver.get(url)
time.sleep(3)

#step4.검색창에 키워드 입력 후 엔터
search_box = driver.find_element_by_css_selector("textarea.gLFyf")
search_box.send_keys(query)
search_box.send_keys(Keys.RETURN)
time.sleep(3)

#step5.동영상 탭 클릭
driver.find_element_by_xpath('//*[@id="hdtb-msb"]/div[1]/div/div[4]').click()
time.sleep(2)

#step6.동영상 추출
video_links = driver.find_elements_by_css_selector("div.VYkpsb")
link_video = []
for video in video_links:
    link = video.get_attribute('data-url')
    if link is not None:
        link_video.append(link)

#step7.동영상 저장할 폴더 생성
path_folder = '/Users/hunmi/Downloads/video_download/'
if not os.path.isdir(path_folder):
    os.mkdir(path_folder)

#step8.동영상 다운로드
i = 0
for link in link_video:
    i += 1
    urlretrieve(link, path_folder + query + f'{i}.mp4')
