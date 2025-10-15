# 🎙️ Voice GenAI Tool | Voice Cloning, Transcription, Real-time AI

![Coverage](https://img.shields.io/badge/coverage-check_pytest--cov-blue?style=for-the-badge)

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

## 📊 Coverage Setup

To generate test coverage reports:

```bash
# Install pytest-cov
pip install pytest-cov

# Run tests with coverage
pytest --cov=src --cov-report=html --cov-report=term

# View HTML report
open htmlcov/index.html
```

---
