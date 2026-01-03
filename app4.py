import perth
import librosa

AUDIO_PATH = "test-turbo.wav"

# 워터마크된 오디오 로드
watermarked_audio, sr = librosa.load(AUDIO_PATH, sr=None)

# 워터마커 초기화
watermarker = perth.PerthImplicitWatermarker()

# 워터마크 추출
watermark = watermarker.get_watermark(watermarked_audio, sample_rate=sr)
print(f"추출된 워터마크: {watermark}")
# 출력: 0.0 (워터마크 없음) 또는 1.0 (워터마크 있음)