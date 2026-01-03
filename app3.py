import torchaudio as ta
from chatterbox.tts import ChatterboxTTS

# Original 모델 로드
model = ChatterboxTTS.from_pretrained(device="cuda")

# 기본 TTS
text = "The quick brown fox jumps over the lazy dog."
wav = model.generate(text)
ta.save("test-original.wav", wav, model.sr)

# 음성 복제 (오디오 프롬프트 지정)
AUDIO_PROMPT_PATH = "my-voice.wav"
wav = model.generate(text, audio_prompt_path=AUDIO_PROMPT_PATH)
ta.save("test-voice-clone.wav", wav, model.sr)