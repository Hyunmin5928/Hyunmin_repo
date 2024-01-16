from PIL import Image
import numpy as np

# image display에서 사용할 부분 PIL 라이브러리 이용
img = Image.new('RGB', (512, 512))
pix = img.load()

# 1-bit 이미지를 읽어옵니다.
with open('Multimedia/lena512_1bit.raw', 'rb') as file:
    # 1-bit 이미지 데이터를 읽어옵니다.
    image_data = file.read()
    
# 1-bit 데이터를 8-bit로 확장하여 그레이스케일 값으로 변환
for j in range(512):
    for i in range(64):
        byte_value = image_data[(j * 64) + i]
        for k in range(8):
            pixel_value = (byte_value >> k) & 1
            pix[i*8 + k , j] = (pixel_value* 255,pixel_value * 255,pixel_value * 255)
# 이미지를 화면에 표시
img.show()
