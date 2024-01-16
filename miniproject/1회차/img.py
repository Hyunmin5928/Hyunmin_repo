from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.parse import quote_plus

#다운로드 폴더 경로
#download_folder = 'C:/Users/hunmi/img'

# 검색할 키워드 입력(네이버)
query = input('다운로드할 사진에 대한 키워드를 입력하세요: ')

# 이미지 검색 URL 생성
baseurl = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query='
url = baseurl + quote_plus(query)

# HTML 파싱
html = urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
img = soup.find_all(class_='_img')

n = 1
for i in img:
    imgUrl = i['data-source']
    with urlopen(imgUrl) as f:
        with open('./img' + query + str(n) + '.jpg', 'wb') as h:
            img = f.read()
            h.write(img)
    n += 1        

print('다운로드 완료')
