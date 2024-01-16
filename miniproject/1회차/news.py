#step1.프로젝트에 필요한 패키지 불러온다.
from bs4 import BeautifulSoup as bs
import requests

#step2.크롤링할 url 주소를 입력한다. (네이버에서 사건사고 검색 후, 뉴스 탭 클릭하였음)
#url = 'https://search.naver.com/search.naver?where=news&sm=tab_jum&query=사건사고'

#step2-1.만약 키워드를 매번 다르게 입력하고 싶다면 아래와 같이 구성하기.
query = input('검색할 키워드를 입력하세요: ')
url = 'https://search.naver.com/search.naver?where=news&sm=tab_jum&query='+'%s'%query

#step3.requests 패키지의 함수를 이용해 url의 html 문서를 가져온다.
response = requests.get(url)
html_text=response.text

#step4.bs4 패키지의 함수를 이용해서 html 문서를 파싱한다.
soup = bs(html_text, 'html.parser')

#step5.bs4 패키지의 select_one 함수와 선택자 개념을 이용해서 뉴스기사 제목을 하나 가져온다.
#print(soup.select_one('a.news_tit').get_text())

#step6.bs4 패키지의 select 함수와 선택자 개념을 이용해서 뉴스기사 제목을 모두 가져온다.
titles = soup.select('a.news_tit')

for i in titles:
    title = i.get_text()
    print(title)
