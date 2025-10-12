# 🎙️ Voice GenAI Tool | Voice Cloning, Transcription, Real-time AI

<div align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Whisper](https://img.shields.io/badge/Whisper-000000?style=for-the-badge&logo=openai&logoColor=white)
![ElevenLabs](https://img.shields.io/badge/ElevenLabs-FF6B00?style=for-the-badge&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![WebSocket](https://img.shields.io/badge/WebSocket-3b82f6?style=for-the-badge)

</div>

## 🎯 Job Pitch for Recruiters

> Production-grade voice AI platform showcasing expertise in ASR, TTS, real-time streaming, and Python backend engineering. Suitable for AI/GenAI/Python roles.

- Sub-500ms streaming latency with chunked WebSocket pipeline
- High-quality TTS with multilingual support and voice cloning
- End-to-end architecture with deployable Docker setup

---

## 🚀 Features

- Voice cloning from reference samples (ethical guardrails)
- Real-time transcription (Whisper/VAD)
- Multilingual TTS (ElevenLabs/Coqui)
- Streaming conversation loop (ASR -> LLM -> TTS)
- Speaker diarization and profanity filtering
- Export transcripts and audio segments

---

## 🧱 Tech Stack

- Python, FastAPI, WebSocket, uvicorn
- Whisper ASR, TTS (ElevenLabs or Coqui)
- Queueing with asyncio, ffmpeg for audio ops
- Optional: Redis for pub/sub streaming

---

## 🏃 Quick Start

```bash
# Clone
git clone https://github.com/VinodHatti7019/Voice-GenAI-Tool
cd Voice-GenAI-Tool

# Setup
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env  # add ELEVENLABS_API_KEY

# Run backend
uvicorn app.main:app --reload

# Run sample client
python clients/realtime_client.py
```

---

## 📚 Sample Usage (Python)

```python
from app.voice import VoicePipeline

pipe = VoicePipeline(model="whisper", tts="elevenlabs")
segments = pipe.transcribe("sample.wav")
audio = pipe.speak("Hello, this is a voice test", voice_id="Rachel")
```

---

## 🧠 Architecture

- Input: mic -> VAD -> chunks -> ASR
- Orchestration: async tasks, queues, callbacks
- Output: text -> LLM (optional) -> TTS -> stream to client
- Monitoring: latency metrics, error tracking hooks

---

## 🔐 Compliance & Safety

- Consent-based voice cloning prompts
- PII redaction and content moderation
- Configurable retention policy

---

## 🧭 Roadmap

- [ ] Realtime LLM streaming with function-calling
- [ ] Emotion-aware TTS selection
- [ ] Multi-speaker meeting transcription

---

## 📞 Contact

- Email: officialvinodhatti@gmail.com
- LinkedIn: https://www.linkedin.com/in/vinodhatti/
- Portfolio: https://tryliate.com
