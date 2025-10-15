# 🎙️ Voice GenAI Tool | Voice Cloning, Transcription, Real-time AI

![Coverage](https://img.shields.io/badge/coverage-check_pytest--cov-blue?style=for-the-badge)
![GitHub stars](https://img.shields.io/github/stars/VinodHatti7019/Voice-GenAI-Tool?style=for-the-badge)
![GitHub issues](https://img.shields.io/github/issues/VinodHatti7019/Voice-GenAI-Tool?style=for-the-badge)
![GitHub last commit](https://img.shields.io/github/last-commit/VinodHatti7019/Voice-GenAI-Tool?style=for-the-badge)
![License](https://img.shields.io/badge/license-MIT-green?style=for-the-badge)

<div align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Whisper](https://img.shields.io/badge/Whisper-000000?style=for-the-badge&logo=openai&logoColor=white)
![ElevenLabs](https://img.shields.io/badge/ElevenLabs-FF6B00?style=for-the-badge&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![WebSocket](https://img.shields.io/badge/WebSocket-3b82f6?style=for-the-badge)

</div>

> ## 🎯 Job Pitch for Recruiters
>
> Production-grade voice AI platform showcasing expertise in ASR, TTS, real-time streaming, and Python backend engineering. Suitable for AI/GenAI/Python roles.
> - Sub-500ms streaming latency with chunked WebSocket pipeline
> - High-quality TTS with multilingual support and voice cloning
> - End-to-end architecture with deployable Docker setup

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

---

## 📦 Installation

### Prerequisites

- Python 3.8+
- ffmpeg
- API keys (ElevenLabs, OpenAI, etc.)

### Steps

```bash
# Clone the repository
git clone https://github.com/VinodHatti7019/Voice-GenAI-Tool.git
cd Voice-GenAI-Tool

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env with your API keys

# Run the server
uvicorn main:app --reload
```

---

## 🧪 Testing & Coverage

### Run Tests

```bash
# Run all tests
pytest tests/

# Run with coverage
pytest --cov=. --cov-report=term-missing

# Generate HTML coverage report
pytest --cov=. --cov-report=html
```

### Setup pytest-cov

```bash
pip install pytest pytest-cov
```

The coverage badge shows testing infrastructure readiness. Run the commands above to see detailed coverage metrics.

---

## 📚 Documentation

- **[UI Guide](docs/ui_guide.md)** - Complete walkthrough of the web interface
- **[Contributing](CONTRIBUTING.md)** - How to contribute to this project
- **[Advanced Tests](tests/test_advanced.py)** - Integration and advanced test cases

---

## 🤝 Contributing

We welcome contributions! Please check out our [Contributing Guide](CONTRIBUTING.md) to get started.

### Quick Start for Contributors

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'feat: add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

See our [Contributing Guide](CONTRIBUTING.md) for detailed guidelines on:
- Code style and standards
- Testing requirements
- Commit message conventions
- Development setup

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🌟 Show Your Support

If you find this project useful, please consider giving it a ⭐️ on GitHub!

---

## 📬 Contact

- GitHub: [@VinodHatti7019](https://github.com/VinodHatti7019)
- Project Link: [https://github.com/VinodHatti7019/Voice-GenAI-Tool](https://github.com/VinodHatti7019/Voice-GenAI-Tool)

---

## 🙏 Acknowledgments

- OpenAI Whisper for speech recognition
- ElevenLabs for text-to-speech
- FastAPI for the web framework
- All contributors who help improve this project
