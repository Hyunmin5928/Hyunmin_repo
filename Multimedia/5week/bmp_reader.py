from PIL import Image

# Close를 따로 작성 할 필요가 없게 구성
with open('Multimedia/forestfire.bmp', 'rb') as file:
    data = file.read()

# from_bytes 는 기본적으로 'big' 
# BMP 헤더에서 필요한 정보를 추출하기
bfoffBits = int.from_bytes(data[0x0a:0x0e], 'little') 
biWidth = int.from_bytes(data[0x12:0x16], 'little')
biHeigth = int.from_bytes(data[0x16:0x1a],'little')

# 표시 될 이미지 초기 설정
img = Image.new(mode='RGB', size=(biWidth,biHeigth))
pix = img.load()

for j in range(biHeigth):
    for i in range(biWidth):
        # 파란색, 초록색, 빨간색 순서로 읽어오기
        blue = data[bfoffBits]
        green = data[bfoffBits + 1]
        red = data[bfoffBits + 2]
        # pix값 (rgb)설정
        pix[i, biHeigth - j - 1] = (red, green, blue)
        # 다음 pix값(r,g,b)로 이동하기
        bfoffBits += 3
    # 패딩 (행의 길이를 4바이트의 배수로 맞추기)
    padding_bytes = (4 - ((biWidth * 3) % 4)) % 4
    #print(padding_bytes)
    bfoffBits += padding_bytes
# 이미지 표시    
img.show()