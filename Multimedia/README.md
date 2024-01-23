
# Multimedia 과제물

## 3주차

### rawto1bit.py

1. lena512.raw(262,144Byte - 256KB) 파일을 1bit 파일 형식으로 저장
2. 1bit 파일 크기는 32,768Byte - 32KB
3. 파일이름은 lena512_1bit.raw로 저장

### 1bit_raw_open

- rawto1bit.py에서 저장한 lena512_1bit.raw를 다시 읽어서 화면에 display

### 개발 환경

- Python (PIL 모듈 활용)

## 4주차

### 1bit_dithering.py

1. lena512.raw파일을 1bit dithering
2. dither matrix 는 2*2, 4*4 크기를 각각 적용
3. 서로 비교해서 차이점 확인해보기
- 결과 : 4*4 dither matrix를 사용한 쪽이 더 선명하게 나옴

### 개발 환경

- Python (PIL 모듈 활용)

## 5주차

### bmp_reader

1. forestfire.bmp 파일을 byte단위로 읽어서 헤더 파싱
2. pixel image data를 직접 읽어서 화면에 display
- 참고 : BMP file format을 참조하여 작성하였음

### 개발 환경

- Python (PIL 모듈 활용)

## 9주차

### midi.py

1. 120BPM 속도의 악보를 MIDI 파일로 작성하기

### 개발 환경

- Python (midiutil 모듈 활용)

## 10주차

### JPEG.py

1. lena512.raw display
2. 8*8 block based Forward DCT 수행
3. DCT Coefficients를 Quantization 수행
4. Quantization을 수행한 DCT Coefficients를 Q-table를 이용하여 De-Quantization 수행
5. De-Q data를 8*8 block based Inverse DCT 수행
6. 최종 결과 화면에 display
7. 원본과 최종 결과를 비교하여 Block Artifict 현상 확인

- JPEG 표준문서 :  ISO/IEC 10918 - 1 : 1993(E) CCITT Rex. T.81 (1992 E) 참고
- 2번 참고사항 : Annex A.3.3 FDCT and IDCT (informative) 수식 이용
- 3번 참고사항 : Annex K.1 Table K.1 Luminance quantization table 사용, Annex A.3.4 Rounding Operation 준수

### 개발 환경

- Python (PIL 모듈 활용)
