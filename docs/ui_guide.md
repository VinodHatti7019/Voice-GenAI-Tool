# 🖥️ UI Guide - Voice GenAI Tool Frontend

Comprehensive guide for using the Voice GenAI Tool web interface.

---

## 🎯 Overview

The Voice GenAI Tool provides an intuitive web-based UI for:
- **Real-time voice transcription** (Whisper ASR)
- **Text-to-speech generation** (ElevenLabs/Coqui TTS)
- **Voice cloning** from reference samples
- **Streaming conversation loops** (ASR → LLM → TTS)
- **Transcript export** and audio management

---

## 🚀 Getting Started

### 1. Launch the Application

```bash
# Start backend server
cd Voice-GenAI-Tool
python src/main.py

# Start frontend (in another terminal)
cd frontend
npm install
npm start
```

### 2. Access the Web Interface

Open your browser and navigate to:
```
http://localhost:3000
```

---

## 🎤 Main Interface Components

### Landing Page

![Landing Page Screenshot]

**Features:**
- Welcome banner with feature highlights
- Quick action buttons for main features
- Status indicator for backend connection
- Settings and configuration access

**Navigation:**
- **Transcribe** - Real-time speech-to-text
- **Synthesize** - Text-to-speech generation
- **Voice Clone** - Create custom voice profiles
- **Conversation** - Interactive AI chat with voice

---

## 🎯 Feature Guides

### 1. Real-Time Transcription

![Transcription Interface]

#### How to Use:

1. **Select Input Source**
   - Click on "Microphone Input" or "Upload Audio File"
   - Grant microphone permissions if prompted

2. **Configure Settings**
   - **Language**: Select target language (auto-detect available)
   - **Model**: Choose Whisper model (tiny/base/small/medium/large)
   - **VAD Threshold**: Adjust voice activity detection sensitivity

3. **Start Transcription**
   - Click the **"Start Recording"** button
   - Speak clearly into your microphone
   - Watch real-time transcription appear in the text area

4. **Controls**
   - ▶️ **Start**: Begin recording/transcription
   - ⏸️ **Pause**: Temporarily pause recording
   - ⏹️ **Stop**: End recording session
   - 💾 **Export**: Download transcript as .txt or .json

#### Features:
- **Live transcription** with < 500ms latency
- **Speaker diarization** (identifies multiple speakers)
- **Timestamp markers** for each segment
- **Edit capability** for corrections
- **Copy to clipboard** with one click

---

### 2. Text-to-Speech Synthesis

![TTS Interface]

#### How to Use:

1. **Enter Text**
   - Type or paste text into the input area
   - Supports up to 5,000 characters per request

2. **Select Voice**
   - Choose from pre-loaded voices
   - Or use a custom cloned voice (see Voice Clone section)
   - Preview voice with sample playback

3. **Adjust Settings**
   - **Speed**: Control speaking rate (0.5x - 2.0x)
   - **Pitch**: Adjust voice pitch (-12 to +12 semitones)
   - **Stability**: Voice consistency (0-100%)
   - **Clarity**: Voice clarity enhancement (0-100%)

4. **Generate Speech**
   - Click **"Generate Audio"**
   - Progress indicator shows generation status
   - Audio player appears when ready

5. **Audio Controls**
   - ▶️ **Play**: Listen to generated audio
   - 💾 **Download**: Save as MP3/WAV
   - 🔄 **Regenerate**: Create new version with different settings

#### Advanced Options:
- **Style Transfer**: Apply emotional tones (happy, sad, angry, etc.)
- **SSML Support**: Use Speech Synthesis Markup Language for fine control
- **Batch Processing**: Generate audio for multiple texts

---

### 3. Voice Cloning

![Voice Clone Interface]

#### How to Clone a Voice:

1. **Upload Reference Samples**
   - Click **"Add Voice Sample"**
   - Upload 3-5 audio files (5-30 seconds each)
   - Supported formats: WAV, MP3, FLAC, OGG
   
   **Best Practices:**
   - Use high-quality recordings (44.1kHz or higher)
   - Ensure minimal background noise
   - Include varied speaking styles and emotions
   - Minimum 15 seconds total audio required

2. **Voice Profile Setup**
   - **Name**: Enter a name for the voice
   - **Description**: Add notes about the voice
   - **Language**: Select primary language

3. **Training Process**
   - Click **"Create Voice Clone"**
   - Training typically takes 2-5 minutes
   - Progress bar shows training status
   - You'll be notified when complete

4. **Test & Use**
   - Preview with sample text
   - Adjust voice parameters if needed
   - Voice now available in TTS dropdown

#### Ethical Guidelines:
- ⚠️ Only clone voices with explicit permission
- Use responsibly and legally
- Respect privacy and consent requirements

---

### 4. Streaming Conversation

![Conversation Interface]

#### How to Use:

1. **Setup Conversation**
   - Select AI model (GPT-3.5/GPT-4)
   - Choose TTS voice for AI responses
   - Configure conversation context/system prompt

2. **Start Conversation**
   - Click **"Start Conversation"**
   - Microphone activates automatically
   - Speak your message

3. **Conversation Flow**
   - Your speech → ASR transcription → LLM processing → TTS response
   - Visual indicators show each stage
   - AI response plays automatically

4. **Controls**
   - 🎤 **Push-to-Talk**: Hold to speak
   - 🔇 **Mute**: Temporarily disable microphone
   - ⏸️ **Pause AI**: Stop AI from responding
   - 🗑️ **Clear History**: Reset conversation

#### Features:
- **Context awareness**: AI remembers conversation history
- **Interrupt capability**: Stop AI mid-response
- **Real-time streaming**: Low-latency responses
- **Export conversation**: Save as transcript

---

## ⚙️ Settings & Configuration

### General Settings

![Settings Panel]

- **API Keys**
  - OpenAI API Key (for Whisper/GPT)
  - ElevenLabs API Key (for TTS)
  - Configure in `.env` or Settings panel

- **Audio Settings**
  - Input Device: Select microphone
  - Output Device: Select speakers/headphones
  - Sample Rate: 16kHz (standard) / 44.1kHz (high quality)
  - Audio Format: WAV / MP3 / FLAC

- **Performance**
  - Model Size: Trade-off between speed and accuracy
  - Chunk Size: Streaming buffer size
  - Max Concurrent Requests: Rate limiting

- **Privacy**
  - Data Retention: Auto-delete after X days
  - Local Processing: Use on-device models
  - Analytics: Enable/disable usage tracking

---

## 📊 Dashboard & Analytics

![Dashboard View]

### Usage Statistics:
- Total transcriptions/generations this month
- API usage and costs
- Voice clone inventory
- Recent activity log

### Performance Metrics:
- Average transcription latency
- TTS generation time
- Success/error rates
- API response times

---

## 📱 Responsive Design

The UI is fully responsive and works on:
- **Desktop**: Full feature access
- **Tablet**: Optimized layout
- **Mobile**: Core features with touch-friendly controls

---

## 🔧 Troubleshooting

### Common Issues:

#### Microphone Not Working
1. Check browser permissions (allow microphone access)
2. Verify correct input device selected in Settings
3. Test microphone in system settings
4. Try different browser (Chrome/Firefox recommended)

#### Backend Connection Failed
1. Ensure backend server is running (`python src/main.py`)
2. Check console for error messages
3. Verify WebSocket connection at `ws://localhost:8000/ws`
4. Check firewall/antivirus settings

#### TTS Not Generating
1. Verify API key is configured correctly
2. Check API quota/limits not exceeded
3. Review text for unsupported characters
4. Try selecting different voice model

#### Poor Transcription Accuracy
1. Increase microphone input volume
2. Reduce background noise
3. Speak clearly and at moderate pace
4. Try larger Whisper model (e.g., medium/large)
5. Adjust VAD threshold in settings

---

## 🎓 Tips & Best Practices

### For Best Transcription Results:
- Use a quality microphone (USB or headset recommended)
- Record in a quiet environment
- Speak naturally at conversational pace
- Use the "large" model for maximum accuracy
- Enable punctuation auto-formatting

### For Best TTS Results:
- Write in natural, conversational language
- Use punctuation to control pacing
- Break long texts into paragraphs
- Experiment with voice settings
- Use SSML tags for advanced control

### For Voice Cloning:
- Use multiple 10-15 second samples
- Include varied emotions and tones
- Ensure consistent recording quality
- Avoid background noise and echo
- Test thoroughly before production use

---

## 🔑 Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| `Ctrl/Cmd + R` | Start Recording |
| `Ctrl/Cmd + S` | Stop Recording |
| `Ctrl/Cmd + E` | Export Transcript |
| `Ctrl/Cmd + G` | Generate TTS |
| `Ctrl/Cmd + Space` | Play/Pause Audio |
| `Ctrl/Cmd + ,` | Open Settings |
| `Esc` | Cancel Current Operation |

---

## 📦 Export Options

### Transcript Export Formats:
- **TXT**: Plain text transcript
- **JSON**: Structured data with timestamps
- **SRT**: Subtitle format for videos
- **VTT**: Web video text tracks

### Audio Export Formats:
- **MP3**: Compressed (default)
- **WAV**: Uncompressed high quality
- **FLAC**: Lossless compression
- **OGG**: Open format

---

## 📞 Support & Resources

- **Documentation**: [Full API Reference](/docs/api_reference.md)
- **Architecture**: [System Design](/docs/architecture.md)
- **Issues**: [GitHub Issues](https://github.com/VinodHatti7019/Voice-GenAI-Tool/issues)
- **Contributing**: [Contribution Guidelines](/CONTRIBUTING.md)

---

## 📸 Screenshot Guide

**Note**: This guide references UI screenshots. To add screenshots:

1. Capture screenshots of each interface section
2. Save as PNG files in `/docs/images/` directory:
   - `landing_page.png`
   - `transcription_interface.png`
   - `tts_interface.png`
   - `voice_clone_interface.png`
   - `conversation_interface.png`
   - `settings_panel.png`
   - `dashboard_view.png`

3. Update this document with image links:
   ```markdown
   ![Landing Page](images/landing_page.png)
   ```

---

## ✅ Feature Checklist

- [x] Real-time transcription
- [x] Text-to-speech synthesis
- [x] Voice cloning
- [x] Streaming conversations
- [x] Multi-language support
- [x] Export functionality
- [x] Responsive design
- [x] Dark/Light themes
- [x] Keyboard shortcuts
- [x] Dashboard analytics

---

**Last Updated**: October 2025  
**Version**: 2.0.0  
**Maintained by**: VinodHatti7019
