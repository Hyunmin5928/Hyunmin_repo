# Django project

### 벤처사업아카데미 miniproject 4회차
-기간 : 2023.06.08 ~ 2023.06.29

## 초기 설정

### config/settings.py
- mysql 접속을 위한 부분을 설정
- static 디자인 파일 활용을 위한 부분 추가

### static 파일에 디자인 파일 추가

## templates/ 

### 구성 내용
- base.html, home.html, navbar.html, footer.html
   위의 html파일로 웹사이트의 UI 디자인
- board_write.html, board_view.html, board_list.html, board_edit.html
   위의 html파일로는 board/에 작성한 함수를 호출하는 기능 및 게시판 UI구성

## board/

- mysql과 연동시켜주는 부분, 실제 게시글이 작성, 조회, 추가, 삭제 되는 기능을 수행하는 부분

## 개발 환경 :
- Python
- Django
- Mysql
