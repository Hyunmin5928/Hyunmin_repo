# Capstone 

## 졸업작품 'TTS를 활용한 동화책 애플리캐이션' Audio Streaming Server-Client 코드

## 개발 배경 

- 클라이언트와 서버간의 통신 속도를 고려하여 UDP 통신 프로토콜 활용 결정

## Server 측 

### 작동 방식 : 

1. client의 요청이 있을 때까지 대기
2. 요청(화자, 대사, 감정)이 담긴 text가 오면, 해당 정보를 tacotron vae모델에 전송
3. 모델이 생성한 wav파일의 audio data만 추출하여 여러 packet을 분할하여 전송
4. 전송 속도에 제한을 두기 위해 딜레이를 설정
5. client에게 모든 데이터를 전송한 후에는 연결을 종료

- 딜레이를 설정하지 않았을 떄, audio data가 클 경우 누락되는 현상이 발생되어 설정
- 실시간 재생을 위해 이에 영향을 주지 않을 정도의 delay를 설정하였음

### 사용 환경 :

- Python
- Tacotron2 모델 및 관련 의존성 설치 필요

## Client 측 (Unity 앱)

### 작동 방식 :

1. 동화책의 화자, 대사, 감정 정보를 포함한 Text data를 server에 전송
2. server측에서 생성 된 wav파일의 여러 packet으로 분할 된 audio data를 수신
3. 수신 된 audio data를 재결합, wav header를 추가하여 wav파일로 저장 및 재생
4. Unity 앱에서 wav파일 재생 

### 사용 환경 :

- C#
- Unity 2019.4 이상

## 유의 사항 :

- port번호, ip주소 실제 서버 정보로 정확하게 설정하기