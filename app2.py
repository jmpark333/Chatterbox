import torchaudio as ta
from chatterbox.mtl_tts import ChatterboxMultilingualTTS

# Multilingual 모델 로드
multilingual_model = ChatterboxMultilingualTTS.from_pretrained(device="cuda")

# 한국어 예시
korean_text = "안녕하세요, 오늘 날씨가 정말 좋네요. 즐거운 주말 보내시길 바랍니다."
wav_korean = multilingual_model.generate(korean_text, language_id="ko")
ta.save("test-korean.wav", wav_korean, multilingual_model.sr)

# 영어 예시
english_text = "Ezreal and Jinx teamed up with Ahri, Yasuo, and Teemo to take down the enemy's Nexus."
wav_english = multilingual_model.generate(english_text, language_id="en")
ta.save("test-english.wav", wav_english, multilingual_model.sr)

# 프랑스어 예시
french_text = "Bonjour, comment ça va? Ceci est le modèle de synthèse vocale multilingue Chatterbox."
wav_french = multilingual_model.generate(french_text, language_id="fr")
ta.save("test-french.wav", wav_french, multilingual_model.sr)

# 중국어 예시
chinese_text = "你好，今天天气真不错，希望你有一个愉快的周末。"
wav_chinese = multilingual_model.generate(chinese_text, language_id="zh")
ta.save("test-chinese.wav", wav_chinese, multilingual_model.sr)