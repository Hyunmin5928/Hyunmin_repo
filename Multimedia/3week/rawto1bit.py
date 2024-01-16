# 읽는 file, 쓰는 file 2가지로 생성 
in_file = open('Multimedia/lena512.raw', 'rb')
out_file = open('Multimedia/lena512_1bit.raw', 'wb')

# 상수 선언
Img_size = 512*512
Num_byte = 8

b = bytearray(1)
for i in range(Img_size // Num_byte):
    data = in_file.read(8)  # 8byte씩 읽기
    b[0] = 0b00000000
    for j in range(Num_byte):
        # 비트 연산실시
        b[0] |= 0b00000001  << j if data[j] > 127 else 0b00000000
    #print(b)
    out_file.write(b)

in_file.close()
out_file.close()



