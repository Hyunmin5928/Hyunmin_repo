using UnityEngine;
using System.IO;
using System.Net.Sockets;
using System.Threading.Tasks;
using System.Text;

public class AudioStreamingClient : MonoBehaviour
{
    public string serverHost = "114.70.63.57"; // 서버 IP 주소
    public int serverPort = 20003; // 서버 포트 번호

    private UdpClient udpClient;
    private AudioSource audioSource;
    private MemoryStream audioDataStream;

    private bool isReceiving;       // 패킷수신 상태를 보여줌
    private int receivedPacketCount;    // 수신한 패킷 수를 나타냄

    private bool isLastPacket;
    private int expectedPacketCount;   // 기대되는 패킷 수를 나타냄
    private bool isLastPacketReceived; // 마지막 패킷을 받았는지 여부를 나타냄

    // 패킷 재조립을 위한 변수들
    private int bufferSize = 16192;
    private byte[][] packetBuffer; // 패킷을 저장하는 버퍼
    private bool[] packetReceived; // 각 패킷이 도착했는지 여부를 나타내는 배열

    private void Start()
    {
        audioSource = GetComponent<AudioSource>();

        if (audioSource == null)
            audioSource = gameObject.AddComponent<AudioSource>();

        audioSource.volume = 0.5f;
        audioSource.loop = true;
        audioSource.spatialBlend = 1.0f;

        udpClient = new UdpClient();
        udpClient.Connect(serverHost, serverPort);

        Debug.Log($"서버에 연결됨: {serverHost}:{serverPort}");

        audioDataStream = new MemoryStream();

        isReceiving = true;
        receivedPacketCount = 0;

        // 패킷 재조립을 위한 초기화
        packetBuffer = new byte[bufferSize][];
        packetReceived = new bool[bufferSize];

        _ = ReceiveUDPData(); // 패킷 수신 대기
    }

    private async Task ReceiveUDPData()
    {
        byte[] audioDataBuffer = new byte[bufferSize];

        isLastPacket = false; // 마지막 패킷인지 확인하기 위한 변수
        expectedPacketCount = 0;
        isLastPacketReceived = false;

        while (isReceiving)
        {
            try
            {
                UdpReceiveResult result = await udpClient.ReceiveAsync();
                byte[] packetData = result.Buffer;
                Debug.Log("서버에서 UDP 패킷 수신");

                if (packetData.Length > 0)
                {
                    Debug.Log($"오디오 data 패킷 크기: {packetData.Length} bytes");

                    int packetNumber = packetData[0] >> 1;
                    if (expectedPacketCount == 0)
                    {
                        expectedPacketCount = packetData[1]; // 패킷 헤더의 마지막 비트에 전체 패킷 수 저장
                    }
                    packetReceived[packetNumber] = true; // 해당 패킷을 수신한 것으로 표시

                    // 패킷 정보 로깅
                    Debug.Log($"패킷 번호: {packetNumber}, 패킷 총 갯수 : {expectedPacketCount}, 패킷 크기: {packetData.Length}");

                    // 패킷의 앞 2바이트는 패킷 번호와 전체 패킷 수이므로 제외
                    byte[] audioData = new byte[packetData.Length - 2];
                    System.Array.Copy(packetData, 2, audioData, 0, audioData.Length);
                    packetBuffer[packetNumber] = audioData; // 해당 패킷을 버퍼에 저장
                    packetReceived[packetNumber] = true;

                    // 수신한 패킷 수 증가
                    receivedPacketCount++;
                    Debug.Log($"수신 된 패킷개수: {receivedPacketCount}");

                    // 패킷의 끝을 확인하여 전체 WAV 파일을 수신한 경우 재생 및 저장합니다.
                    //if ((packetData[0] + 1) == expectedPacketCount)
                    //{
                    //    isLastPacketReceived = true;  // 패킷 헤더의 첫 번째 비트가 1이면 마지막 패킷임
                    //}
                    // 수신한 패킷의 순서가 기대하는 패킷 번호와 일치하는지 확인
                    if (receivedPacketCount == expectedPacketCount)
                    {
                        // 모든 패킷을 수신했을 때 WAV 파일로 저장합니다.
                        ReassemblePackets();
                        isReceiving = false;
                        isLastPacketReceived = false;
                    }
                }
            }
            catch (SocketException e)
            {
                Debug.LogError($"UDP 패킷 수신 오류: {e.Message}");
            }
        }

    }

    private void ReassemblePackets()
    {
        // 모든 패킷을 수신했는지 확인
        bool allPacketsReceived = true;
        for (int i = 0; i < expectedPacketCount; i++)
        {
            if (!packetReceived[i])
            {
                allPacketsReceived = false;
                break;
            }
        }

        if (allPacketsReceived)
        {
            // 패킷 재조립 및 WAV 파일 생성
            byte[] audioData = new byte[expectedPacketCount * (bufferSize - 2)];
            int index = 0;
            for (int i = 0; i < expectedPacketCount; i++)
            {
                System.Array.Copy(packetBuffer[i], 0, audioData, index, packetBuffer[i].Length);
                index += packetBuffer[i].Length;
            }

            // WAV 파일로 저장
            string filePath = Path.Combine(Application.persistentDataPath, "received_audio.wav");
            SaveWavFile(filePath, audioData, 16000);
            Debug.Log($"Saved WAV file: {filePath}");

            // WAV 파일 재생
            PlayWavFile(filePath);

            // 초기화
            ClearPacketBuffer();

            // 재수신 시작
            _ = ReceiveUDPData();
        }
    }

    private void ClearPacketBuffer()
    {
        for (int i = 0; i < bufferSize; i++)
        {
            packetBuffer[i] = null;
            packetReceived[i] = false;
        }

        expectedPacketCount = 0;
        receivedPacketCount = 0;
        isLastPacketReceived = false;
    }

    private void PlayWavFile(string filePath)
    {
        if (audioSource.isPlaying)
            audioSource.Stop();

        AudioClip audioClip = LoadWavFile(filePath);
        if (audioClip != null)
        {
            audioSource.clip = audioClip;
            audioSource.Play();

            Debug.Log("오디오 데이터 수신 및 재생");
            Debug.Log($"샘플 레이트: {audioClip.frequency}");
            Debug.Log($"채널: {audioClip.channels}");
            Debug.Log($"길이: {audioClip.length} 초");
        }
        else
        {
            Debug.LogError("WAV 파일을 로드하는 데 실패했습니다.");
        }
    }

    private AudioClip LoadWavFile(string filePath)
    {
        if (File.Exists(filePath))
        {
            byte[] fileData = File.ReadAllBytes(filePath);

            // AudioClip 생성
            int sampleRate = 16000; // 수정: 적절한 샘플 레이트로 설정 (WAV 파일 생성 시 사용한 샘플 레이트와 동일해야 함)
            int channelCount = 1; // 수정: 적절한 채널 수로 설정 (WAV 파일 생성 시 사용한 채널 수와 동일해야 함)
            AudioClip audioClip = AudioClip.Create("AudioClip", fileData.Length / 2, channelCount, sampleRate, false);
            audioClip.SetData(ToFloatArray(fileData), 0);

            return audioClip;
        }
        else
        {
            Debug.LogError($"파일을 찾을 수 없습니다: {filePath}");
            return null;
        }
    }
    private byte[] CreateWavHeader(int dataLength, int sampleRate)
    {
        // WAV 헤더의 크기는 44 bytes입니다.
        byte[] header = new byte[44];

        // Chunk ID: "RIFF"
        header[0] = (byte)'R';
        header[1] = (byte)'I';
        header[2] = (byte)'F';
        header[3] = (byte)'F';

        // Chunk Size: 데이터 크기 + 헤더 크기 - 8 (RIFF와 Chunk Size를 제외한 크기)
        int chunkSize = dataLength + 36;
        header[4] = (byte)(chunkSize & 0xFF);
        header[5] = (byte)((chunkSize >> 8) & 0xFF);
        header[6] = (byte)((chunkSize >> 16) & 0xFF);
        header[7] = (byte)((chunkSize >> 24) & 0xFF);

        // Format: "WAVE"
        header[8] = (byte)'W';
        header[9] = (byte)'A';
        header[10] = (byte)'V';
        header[11] = (byte)'E';

        // Subchunk1 ID: "fmt "
        header[12] = (byte)'f';
        header[13] = (byte)'m';
        header[14] = (byte)'t';
        header[15] = (byte)' ';

        // Subchunk1 Size: 16 (포맷 데이터의 크기)
        header[16] = 16;
        header[17] = 0;
        header[18] = 0;
        header[19] = 0;

        // Audio Format: 1 (PCM)
        header[20] = 1;
        header[21] = 0;

        // Number of Channels: 1 (단일 채널)
        header[22] = 1;
        header[23] = 0;

        // Sample Rate: 16000 (샘플 레이트)
        header[24] = (byte)(sampleRate & 0xFF);
        header[25] = (byte)((sampleRate >> 8) & 0xFF);
        header[26] = (byte)((sampleRate >> 16) & 0xFF);
        header[27] = (byte)((sampleRate >> 24) & 0xFF);

        // Byte Rate: Sample Rate * Number of Channels * Bits per Sample / 8
        int byteRate = sampleRate * 1 * 16 / 8; // Use the appropriate bit depth
        header[28] = (byte)(byteRate & 0xFF);
        header[29] = (byte)((byteRate >> 8) & 0xFF);
        header[30] = (byte)((byteRate >> 16) & 0xFF);
        header[31] = (byte)((byteRate >> 24) & 0xFF);

        // Block Align: Number of Channels * Bits per Sample / 8
        header[32] = (byte)(1 * 16 / 8); // Use the appropriate bit depth
        header[33] = 0;

        // Bits per Sample: 16
        header[34] = 16;
        header[35] = 0;

        // Subchunk2 ID: "data"
        header[36] = (byte)'d';
        header[37] = (byte)'a';
        header[38] = (byte)'t';
        header[39] = (byte)'a';

        // Subchunk2 Size: 데이터 크기
        header[40] = (byte)(dataLength & 0xFF);
        header[41] = (byte)((dataLength >> 8) & 0xFF);
        header[42] = (byte)((dataLength >> 16) & 0xFF);
        header[43] = (byte)((dataLength >> 24) & 0xFF);

        return header;
    }
    private void SaveWavFile(string filePath, byte[] audioData, int sampleRate)
    {
        using (FileStream fileStream = new FileStream(filePath, FileMode.Create))
        {
            // Create WAV header
            byte[] wavHeader = CreateWavHeader(audioData.Length, sampleRate);

            // Write WAV header
            fileStream.Write(wavHeader, 0, wavHeader.Length);

            // Write audio data
            fileStream.Write(audioData, 0, audioData.Length);
        }
    }
    private float[] ToFloatArray(byte[] byteArray)
    {
        int samples = byteArray.Length / 2;
        float[] floatArray = new float[samples];

        for (int i = 0; i < samples; i++)
        {
            short value = (short)((byteArray[i * 2 + 1] << 8) | byteArray[i * 2]);
            floatArray[i] = value / 32768.0f;
        }

        return floatArray;
    }

    public void SendText(string text)
    {
        byte[] textData = Encoding.UTF8.GetBytes(text);
        try
        {
            udpClient.Send(textData, textData.Length);
            Debug.Log("Text 전송");
        }
        catch (SocketException e)
        {
            Debug.LogError($"Error sending text data: {e.Message}");
        }
    }

    private void OnDestroy()
    {
        udpClient.Close();
        Debug.Log("UDP 클라이언트 종료");
    }
}
