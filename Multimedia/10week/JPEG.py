from PIL import Image
import numpy as np
# Forward DCT
def FDCT(block):
    result = np.zeros_like(block, dtype=np.float64)
    for u in range(8):
        for v in range(8):
            if u == 0:
                cu = 1.0 / np.sqrt(2)
            else :
                cu = 1.0
            if v == 0:
                cv = 1.0 / np.sqrt(2)
            else :
                cv = 1.0
            Svu = 0.0
            for x in range(8):
                for y in range(8):
                    Svu += block[x, y] * np.cos((2 * x + 1) * u * np.pi / 16) * np.cos((2 * y + 1) * v * np.pi / 16)
            result[u, v] = 0.25 * cu * cv * Svu
    return result
# Quantization
def Q(block, q_table):
    return np.round(block / q_table)
# De-Quantization
def De_Q(block, q_table):
    return block * q_table
# Inverse DCT
def IDCT(block):
    result = np.zeros_like(block, dtype=np.float64)
    for x in range(8):
        for y in range(8):
            Syx = 0.0
            for u in range(8):
                for v in range(8):
                    if u == 0:
                        cu = 1.0 / np.sqrt(2)
                    else :
                        cu = 1.0
                    if v == 0:
                        cv = 1.0 / np.sqrt(2)
                    else :
                        cv = 1.0
                    Syx += cu * cv * block[u, v] * np.cos((2 * x + 1) * u * np.pi / 16) * np.cos((2 * y + 1) * v * np.pi / 16)
            result[x, y] = 0.25 * Syx
    return result

# 표시 될 이미지 초기 설정
img = Image.new(mode='RGB', size=(512, 512))
img_ori = Image.new(mode='RGB', size=(512, 512))

# Close를 따로 작성 할 필요가 없게 구성
with open('Multimedia/lena512.raw', 'rb') as file:
    data = file.read()

# original 사진, JPEG 압축 사진
image_ori = img_ori.load()
JPEG_img = img.load()

for y in range(img.height):
    for x in range(img.width):
        image_ori[x, y] = (data[y*img.width+x], data[y*img.width+x], data[y*img.width+x])

# 이미지 데이터를 NumPy 배열로 변환
image_array = np.frombuffer(data, dtype=np.uint8).reshape((512, 512))

# Annex K.1 Table K.1 Luminance quantization table 표준문서 참조
q_table = np.array([[16, 11, 10, 16, 24, 40, 51, 61],
                   [12, 12, 14, 19, 26, 58, 60, 55],
                   [14, 13, 16, 24, 40, 57, 69, 56],
                   [14, 17, 22, 29, 51, 87, 80, 62],
                   [18, 22, 37, 56, 68, 109, 103, 77],
                   [24, 35, 55, 64, 81, 104, 113, 92],
                   [49, 64, 78, 87, 103, 121, 120, 101],
                   [72, 92, 95, 98, 112, 100, 103, 99]])

# 이미지를 8x8 블록으로 처리하며 JPEG 압축 및 이미지 생성
for y in range(0, img.height, 8):
    for x in range(0, img.width, 8):
        block = image_array[y:y+8, x:x+8]
        # Forward DCT 수행
        FDCT_block = FDCT(block)
        # Quantization 수행
        Q_block = Q(FDCT_block, q_table)
        # De-Quantization 수행
        DeQ_block = De_Q(Q_block, q_table)
        # Inverse DCT 수행
        IDCT_block = IDCT(DeQ_block)
        # 최종 Image
        for i in range(8):
            for j in range(8):
                JPEG_img[x + j, y + i] = (int(IDCT_block[i, j]), int(IDCT_block[i, j]), int(IDCT_block[i, j]))
img_ori.show()
img.show()