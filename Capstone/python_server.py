import socket
import wave
import logging

# 로거 설정
logging.basicConfig(level=logging.DEBUG, format='[%(asctime)s] %(message)s')

# 포트번호와 IP주소 설정
host = '0.0.0.0'  # 모든 Network Interface에서 수신이 가능
port = 6006       # 해당 포트번호는 변경해야 함.
buf_size = 4096

# rb모드로 wav파일을 열기
with wave.open('audio.wav', 'rb') as wav_file:
    # UDP소켓 생성, AF_INET : IPv4주소 체계사용, SOCK_DGRAM : UDP프로토콜 사용
    server_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    server_socket.bind((host, port))    # 소켓에 주어진 host와 port를 bind(묶어줌)
    logging.info(f"Server listening on {host}:{port}...")
    while True:         # 무한 루프를 돌면서 UDP패킷을 수신하기 시작
        # Receive incoming UDP packets, 여기에서 클라이언트의 ip주소를 저장
        try:
            packet_data = server_socket.recvfrom(buf_size)

            message = packet_data[0]
            client_address = packet_data[1]
            logging.info("Received packet from client: %s", client_address)
            # 나머지 코드...
            if message.decode() == '안녕하세요':
                logging.info("Received 'get_audio_data' request from client: %s", client_address)

                # Read a certain size of audio data from the WAV file and send it to the client in chunks
                audio_data = wav_file.readframes(buf_size)
                logging.info("Read audio data from the WAV file")

                # If the entire WAV file has been read before reading the specified size, rewind to the beginning
                if audio_data == b'':
                    wav_file.rewind()
                    audio_data = wav_file.readframes(buf_size)
                    logging.info("Rewound the WAV file and read audio data again")

                # Send the audio data to the connected client
                server_socket.sendto(audio_data, client_address)
                logging.info("Sent audio data to the client")

                # If the last chunk of audio data was sent, break the loop
                if len(audio_data) < buf_size:
                    break
        except Exception as e:
            logging.error("Error occurred while receiving packet: %s", str(e))