from PIL import Image

# Close를 따로 작성 할 필요가 없게 구성
with open('Multimedia/lena512.raw', 'rb') as file:
    data = file.read()

# 표시 될 이미지 초기 설정
img1 = Image.new(mode='RGB', size=(512, 512))
pix1 = img1.load()
img2 = Image.new(mode='RGB', size=(512, 512))
pix2 = img2.load()
d1 = ( (0, 2), (3, 1) )
d2 = ( (0, 8, 2, 10), (12, 4, 14, 6), (3, 11, 1, 9), (15, 7, 13, 5))

for y in range(512):
    for x in range(512):
        # d1 dithering
        i1 = x % 2
        j1 = y % 2
        gray1 = 255 if data[y * 512 + x] > d1[j1][i1] * 255 / 3 else 0  
        # pix값 gray sclae 설정
        pix1[x, y] = (gray1, gray1, gray1)


for y in range(512):
    for x in range(512):
        # d2 dithering
        i2 = x % 4
        j2 = y % 4
        gray2 = 255 if data[y * 512 + x] > d2[j2][i2]*16 else 0
        # pix값 gray sclae 설정
        pix2[x, y] = (gray2, gray2, gray2)

# 이미지 표시    
img1.show()
img2.show()