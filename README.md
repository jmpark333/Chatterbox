# 🎙️ Chatterbox: 감정 표현과 음성 복제가 가능한 AI TTS

<div align="center">

![Chatterbox](https://img.shields.io/badge/Chatterbox-AI%20TTS-blue)
![Python](https://img.shields.io/badge/Python-3.11+-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

**Resemble AI의 오픈소스 텍스트-투-스피치(TTS) 모델**

[Chatterbox](https://github.com/resemble-ai/chatterbox)는 제로샷 음성 복제, 감정 태그 지원, 다국어 TTS 기능을 제공하는 최첨단 AI 음성 생성 모델입니다.

[블로그](https://fornewchallenge.tistory.com/) • [데모](https://huggingface.co/spaces/ResembleAI/chatterbox-turbo-demo) • [Star](https://github.com/jmpark333/Chatterbox/stargazers)

</div>

---

## ✨ 주요 특징

| 특징 | 설명 |
|------|------|
| 🎙️ **제로샷 음성 복제** | 단 10초의 참고 음성만으로 목소리 복제 가능 |
| 😊 **감정 태그 지원** | `[laugh]`, `[cough]`, `[chuckle]` 등 자연스러운 감정 표현 |
| ⚡ **초고속 생성** | Turbo 모델은 1단계 디코딩으로 기존 10단계를 1단계로 축소 |
| 🌍 **다국어 지원** | Multilingual 모델은 한국어 포함 23개 언어 지원 |
| 💻 **가벼운 모델** | Turbo 모델은 350M 파라미터로 낮은 VRAM 요구 |
| 🔒 **내장 워터마킹** | 모든 생성 음성에 PerTh 워터마크 자동 포함 |

---

## 📦 설치 방법

### pip로 설치 (추천)

```bash
pip install chatterbox-tts
```

### 소스에서 설치

```bash
# conda 환경 생성 (권장)
conda create -yn chatterbox python=3.11
conda activate chatterbox

# 리포지토리 복제
git clone https://github.com/jmpark333/Chatterbox.git
cd Chatterbox

# 패키지 설치
pip install -e .
```

### ⚠️ 시스템 요구사항

- Python 3.11 권장
- CUDA 지원 GPU (NVIDIA)
- Debian 11에서 개발 및 테스트 완료

---

## 🚀 빠른 시작

### 1. Chatterbox-Turbo 예제 (app.py)

감정 태그가 포함된 음성 생성:

```bash
python app.py
```

**코드 미리보기:**
```python
import torchaudio as ta
from chatterbox.tts_turbo import ChatterboxTurboTTS

# Turbo 모델 로드
model = ChatterboxTurboTTS.from_pretrained(device="cuda")

# 감정 태그가 포함된 텍스트
text = "Hi there, James here from MochaFone calling you back [clear throat], have you got one minute to chat about the billing issue?"

# 음성 생성 (참고 클립 필요)
wav = model.generate(text, audio_prompt_path="my-voice.wav")

# 음성 저장
ta.save("test-turbo.wav", wav, model.sr)
```

### 2. Multilingual 예제 (app2.py)

다국어 음성 생성:

```bash
python app2.py
```

**지원 언어:** 한국어, 영어, 프랑스어, 중국어 등 23개 언어

### 3. Original 모델 예제 (app3.py)

기본 TTS 및 음성 복제:

```bash
python app3.py
```

### 4. 워터마크 추출 예제 (app4.py)

생성된 음성의 워터마크 확인:

```bash
python app4.py
```

---

## 📂 프로젝트 구조

```
Chatterbox/
├── app.py              # Chatterbox-Turbo 예제
├── app2.py             # Multilingual 예제
├── app3.py             # Original 모델 예제
├── app4.py             # 워터마크 추출 예제
├── my-voice.wav        # 음성 복제 참고 오디오
├── test-turbo.wav      # Turbo 생성 샘플
├── test-korean.wav     # 한국어 생성 샘플
├── test-english.wav    # 영어 생성 샘플
├── test-french.wav     # 프랑스어 생성 샘플
├── test-original.wav   # Original 기본 TTS 샘플
└── test-voice-clone.wav # 음성 복제 샘플
```

---

## 🤖 Chatterbox 모델 비교

| 모델 | 크기 | 언어 | 주요 특징 | 추천 용도 |
|------|------|------|------------|-----------|
| **Chatterbox-Turbo** | 350M | 영어 | 감정 태그, 저전력/저VRAM | 실시간 음성 에이전트, 프로덕션 |
| **Chatterbox-Multilingual** | 500M | 23개 언어 | 제로샷 복제, 다국어 | 글로벌 애플리케이션, 현지화 |
| **Chatterbox Original** | 500M | 영어 | CFG & Exaggeration 튜닝 | 창의적 제어가 필요한 TTS |

---

## 🌍 지원 언어 (Multilingual)

아랍어(ar) • 덴마크어(da) • 독일어(de) • 그리스어(el) • 영어(en) • 스페인어(es) • 핀란드어(fi) • 프랑스어(fr) • 히브루어(he) • 힌디어(hi) • 이탈리아어(it) • 일본어(ja) • **한국어(ko)** • 말레이어(ms) • 네덜란드어(nl) • 노르웨이어(no) • 폴란드어(pl) • 포르투갈어(pt) • 러시아어(ru) • 스웨덴어(sv) • 스와힐리어(sw) • 터키어(tr) • **중국어(zh)**

---

## 😊 감정 태그 (Turbo 모델)

| 태그 | 설명 | 예시 |
|------|------|------|
| `[laugh]` | 웃음 | "That's funny [laugh]" |
| `[chuckle]` | 낄낄거림 | "Let me explain [chuckle]" |
| `[cough]` | 기침 | "Excuse me [cough]" |
| `[breath]` | 숨소리 | "Okay [breath]" |

---

## ⚙️ 고급 튜닝 팁 (Original 모델)

### 주요 파라미터

- **cfg_weight** (0.0 ~ 1.0, 기본값 0.5): 낮을수록 자연스러운 말투
- **exaggeration** (0.0 ~ 1.0, 기본값 0.5): 높을수록 더 표현적이고 극적인 음성

### 추천 설정

| 용도 | cfg_weight | exaggeration |
|------|------------|---------------|
| 일반적인 TTS/음성 에이전트 | 0.5 | 0.5 |
| 빠른 말투의 화자 | 0.3 | 0.5 |
| 표현적/극적인 연기 | 0.3 | 0.7+ |

---

## 🔒 워터마크 추출

모든 Chatterbox 생성 음성에는 PerTh (Perceptual Threshold) 워터마크가 포함되어 있습니다.

```python
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
```

---

## 📚 참고 자료

- [Chatterbox GitHub Repository](https://github.com/resemble-ai/chatterbox)
- [Chatterbox-Turbo Demo - Hugging Face](https://huggingface.co/spaces/ResembleAI/chatterbox-turbo-demo)
- [How to Build an AI Voice Agent in Minutes](https://www.resemble.ai/build-ai-voice-agent-minutes/)
- [PerTh Watermarking Library](https://github.com/resemble-ai/perth)
- [Resemble AI Official Website](https://resemble.ai)

---

## 📝 라이선스

이 프로젝트는 학습 및 연구 목적으로 사용할 수 있습니다. Chatterbox 원본 라이선스를 준수하여 사용하세요.

---

<div align="center">

**Made with ❤️ by [jmpark333](https://github.com/jmpark333)**

[⭐ Star](https://github.com/jmpark333/Chatterbox/stargazers) this repo if it helped you!

</div>
