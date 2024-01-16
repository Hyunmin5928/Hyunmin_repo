import socket
import wave
import logging
import subprocess

# 로거 설정
logging.basicConfig(level=logging.DEBUG, format='[%(asctime)s] %(message)s')

# 포트번호와 IP주소 설정
host = '0.0.0.0'  # 모든 Network Interface에서 수신이 가능
port = 6006       # 해당 포트번호는 변경해야 함.
buf_size = 4096

# UDP소켓 생성, AF_INET : IPv4주소 체계사용, SOCK_DGRAM : UDP프로토콜 사용
server_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
server_socket.bind((host, port))  # 소켓에 주어진 host와 port를 bind(묶어줌)
logging.info(f"Server listening on {host}:{port}...")

# 클라이언트 주소 저장을 위한 변수
client_address = None

while True:  # 무한 루프를 돌면서 UDP패킷을 수신하기 시작
    # UDP packet 수신
    try:
        packet_data = server_socket.recvfrom(buf_size)

        message = packet_data[0]
        client_address = packet_data[1]
        logging.info("Received packet from client: %s", client_address)

        # 클라이언트가 'get_audio_data' 메시지를 전송한 경우 WAV 파일을 스트리밍 형식으로 전송
        if message:
            logging.info("Received packet from client: %s", client_address)

            # 메시지를 분리하기 위해 구분자 '|'를 사용하여 분리
            parts = message.split('|')

            # 분리 된 메세지의 맢뒤 공백을 없애는 부분 sprip함수 활용
            if len(parts) == 3:
                # params, 변수들
                text = parts[0].strip()  # 대사 부분
                emo = parts[1].strip()  # 감정 부분
                speaker = parts[2].strip()  # 화자 부분

                # 분리된 부분을 활용하여 작업 수행
                logging.info("Received dialogue: %s", text)
                logging.info("Received emotion: %s", emo)
                logging.info("Received speaker: %s", speaker)
            else:
                logging.error("Invalid message format: %s", message)


            # tacotron-vae모델이 실행되는 부분
            py_path = "/data/vae-taco-hifi-gan/infer.py"  # 추론 스크립트가 존재하는 경로
            taco_interface = "-m Tacotron2 -o output/ -lr 1e-3 --epochs 700 -bs 36"  # 추론시 필요한 인수들(arg parser)
            prefix = "python3" + " " + py_path + " " + taco_interface  # 합치기

            # embedded
            emb_text = "--input" + " " + '"' + text + '"'  # arg parser 형식에 맞게 변형
            emb_emo = "--emotion" + " " + emo  # arg parser 형식에 맞게 변형
            emb_speaker = "--speaker" + " " + speaker  # arg parser 형식에 맞게 변형

            exec_path = prefix + " " + emb_text + " " + emb_emo + " " + emb_speaker  # 최종 실행 명령어
            print(exec_path)  # 최종 실행 명령어 확인

            subprocess.run(exec_path, shell=True)  # 실행, 터미널 또는 셸에서 실행시키는 것과 동일

            with wave.open('/data/vae-taco-hifi-gan/infer_result/result_generated_e2e.wav', 'rb') as wav_file:
                # 읽을 데이터가 남아있을 경우...
                if wav_file.tell() == wav_file.getnframes():
                    wav_file.rewind()

                # 한 번에 읽을 데이터 크기를 지정
                chunk_size = 1024
                audio_data = wav_file.readframes(chunk_size)

                # 데이터를 패킷 단위로 분할하여 클라이언트에게 전송
                while audio_data:
                    server_socket.sendto(audio_data, client_address)
                    audio_data = wav_file.readframes(chunk_size)

                # 클라이언트에게 모든 데이터를 전송한 후에는 연결을 종료
                server_socket.sendto(b'', client_address)
                logging.info("Sent audio data to the client: %s", client_address)

    except Exception as e:
        logging.error("Error occurred while receiving packet: %s", str(e))