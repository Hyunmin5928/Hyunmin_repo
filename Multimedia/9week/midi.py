from midiutil.MidiFile import MIDIFile

# MIDI 파일 생성
midi = MIDIFile(1)

# 트랙 및 시간 설정
track = 0
time = 0

# 120BPM 설정
tempo = 120

# 템포 정보 추가
midi.addTempo(track, time, tempo)

# 악보 데이터 추가 (C, D, E, F, G)
notes = [60, 62, 64, 65, 67, 69, 71, 72]  # 도~도 한 음씩 올라가는 MIDI 노트 번호
durations = [2, 2, 2, 2, 2, 2, 2, 2]    # 쉼표로 활용

# 음표, 박자, 음량 추가
for note, duration in zip(notes, durations):
    midi.addNote(track, 0, note, time, duration, 100)  # 채널 0, 음표, 시작 시간, 음표 길이, 음량
    time += duration    # 쉼표를 표현하는 부분, 다음 음표가 추가되기 위해 기다려지는 시간

# .mid 파일 저장
with open("Multimedia/MIDI.mid", "wb") as MIDI_file:
    midi.writeFile(MIDI_file)