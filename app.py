import torchaudio as ta
import torch
from chatterbox.tts_turbo import ChatterboxTurboTTS

# Turbo 모델 로드
model = ChatterboxTurboTTS.from_pretrained(device="cuda")

# 감정 태그가 포함된 텍스트
text = "Hi there, James here from MochaFone calling you back [clear throat], have you got one minute to chat about the billing issue?"

# 음성 생성 (참고 클립 필요)
wav = model.generate(text, audio_prompt_path="my-voice.wav")

# 음성 저장
ta.save("test-turbo.wav", wav, model.sr)