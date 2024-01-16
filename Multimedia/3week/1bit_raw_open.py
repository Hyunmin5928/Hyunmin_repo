from PIL import Image
import numpy as np

# image display에서 사용할 부분 PIL 라이브러리 이용
img = Image.new('RGB', (512, 512))
pix = img.load()

# 1-bit 이미지를 읽어옵니다.
with open('Multimedia/lena512_1bit.raw', 'rb') as file:
    # 1-bit 이미지 데이터를 읽어옵니다.
    image_data = file.read()

print(image_data)
# 1-bit 데이터를 8-bit로 확장하고 리스트에 추가
for j in range(512):
    for i in range(512):
        tmp = 0b00000000


#for y in range(512):
#    for x in range(512):
#        # 한 줄씩 tmp에 저장 y
#        tmp = 255 if data[y * 512 + x] > 127 else 0
#        pix[x, y] = (tmp, tmp, tmp)

# image display
img.show()


