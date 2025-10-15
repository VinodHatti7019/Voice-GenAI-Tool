# Voice-GenAI-Tool API Reference

## Overview

The Voice-GenAI-Tool provides a comprehensive REST API for integrating voice-enabled AI functionality into applications. This document details all available endpoints, request/response formats, and usage examples.

## Base URL

```
http://localhost:8000
```

## Authentication

Currently, the API does not require authentication. However, you must provide a valid OpenAI API key through environment variables.

## Endpoints

### Health Check

#### `GET /health`

Returns the health status of the application.

**Response**
```json
{
    "status": "healthy",
    "timestamp": "2024-01-15T10:30:00Z",
    "version": "1.0.0",
    "uptime": "2h 30m 45s"
}
```

**Status Codes**
- `200`: Service is healthy
- `503`: Service is unhealthy

---

### Voice Processing

#### `POST /voice/process`

Processes voice input and returns AI-generated response.

**Request Headers**
```
Content-Type: application/json
```

**Request Body**
```json
{
    "action": "listen_and_respond",
    "duration": 5,
    "language": "en-US",
    "response_format": "both",
    "voice_settings": {
        "rate": 150,
        "volume": 0.9
    }
}
```

**Parameters**
- `action` (string, required): Action to perform (`"listen_and_respond"` | `"listen_only"`)
- `duration` (integer, optional): Listening duration in seconds (default: 5)
- `language` (string, optional): Speech recognition language (default: "en-US")
- `response_format` (string, optional): Response format (`"text"` | `"voice"` | `"both"`) (default: "both")
- `voice_settings` (object, optional): Voice synthesis settings
  - `rate` (integer): Speech rate (50-300, default: 150)
  - `volume` (float): Volume level (0.0-1.0, default: 0.9)

**Response**
```json
{
    "success": true,
    "user_input": "What's the weather like today?",
    "ai_response": "I don't have access to real-time weather data, but I can help you find weather information through various weather services or apps.",
    "processing_time": 2.34,
    "voice_file_url": "/audio/response_12345.wav",
    "metadata": {
        "model_used": "gpt-3.5-turbo",
        "tokens_used": 45,
        "confidence_score": 0.95
    }
}
```

**Status Codes**
- `200`: Success
- `400`: Bad request (invalid parameters)
- `500`: Internal server error
- `503`: Service unavailable (microphone/speaker issues)

---

### Text Processing

#### `POST /text/process`

Processes text input and returns AI-generated response.

**Request Body**
```json
{
    "text": "Explain quantum computing in simple terms",
    "response_format": "text",
    "model": "gpt-3.5-turbo",
    "max_tokens": 150,
    "temperature": 0.7
}
```

**Parameters**
- `text` (string, required): Input text to process
- `response_format` (string, optional): Response format (`"text"` | `"voice"` | `"both"`) (default: "text")
- `model` (string, optional): OpenAI model to use (default: "gpt-3.5-turbo")
- `max_tokens` (integer, optional): Maximum response tokens (default: 150)
- `temperature` (float, optional): Response creativity (0.0-2.0, default: 0.7)

**Response**
```json
{
    "success": true,
    "user_input": "Explain quantum computing in simple terms",
    "ai_response": "Quantum computing uses the principles of quantum mechanics to process information in ways that classical computers cannot...",
    "processing_time": 1.23,
    "voice_file_url": null,
    "metadata": {
        "model_used": "gpt-3.5-turbo",
        "tokens_used": 89,
        "finish_reason": "stop"
    }
}
```

---

### Configuration

#### `GET /config`

Returns current application configuration.

**Response**
```json
{
    "voice_settings": {
        "default_language": "en-US",
        "default_rate": 150,
        "default_volume": 0.9,
        "available_voices": ["male", "female"]
    },
    "ai_settings": {
        "default_model": "gpt-3.5-turbo",
        "max_tokens": 150,
        "temperature": 0.7
    },
    "audio_settings": {
        "sample_rate": 16000,
        "channels": 1,
        "chunk_size": 1024
    }
}
```

#### `POST /config`

Updates application configuration.

**Request Body**
```json
{
    "voice_settings": {
        "default_rate": 180,
        "default_volume": 0.8
    },
    "ai_settings": {
        "temperature": 0.8
    }
}
```

**Response**
```json
{
    "success": true,
    "message": "Configuration updated successfully",
    "updated_settings": {
        "voice_settings.default_rate": 180,
        "voice_settings.default_volume": 0.8,
        "ai_settings.temperature": 0.8
    }
}
```

---

### Audio Files

#### `GET /audio/{filename}`

Retrieve generated audio files.

**Parameters**
- `filename` (string): Audio file name from voice processing response

**Response**
- Audio file (WAV format)
- Content-Type: `audio/wav`

**Status Codes**
- `200`: File found
- `404`: File not found
- `410`: File expired

---

## Error Handling

All endpoints return errors in the following format:

```json
{
    "success": false,
    "error": {
        "code": "INVALID_INPUT",
        "message": "The provided text is empty or invalid",
        "details": {
            "field": "text",
            "received": "",
            "expected": "non-empty string"
        }
    }
}
```

### Common Error Codes

| Code | Description | HTTP Status |
|------|-------------|-------------|
| `INVALID_INPUT` | Invalid request parameters | 400 |
| `MISSING_API_KEY` | OpenAI API key not configured | 500 |
| `AUDIO_DEVICE_ERROR` | Microphone/speaker unavailable | 503 |
| `AI_SERVICE_ERROR` | OpenAI API error | 502 |
| `TIMEOUT_ERROR` | Request timeout | 504 |
| `RATE_LIMIT_EXCEEDED` | Too many requests | 429 |

---

## Rate Limits

- Voice processing: 60 requests per minute
- Text processing: 100 requests per minute
- Configuration updates: 10 requests per minute

## Usage Examples

### Python

```python
import requests
import json

# Text processing example
url = "http://localhost:8000/text/process"
payload = {
    "text": "Hello, how are you?",
    "response_format": "both"
}

response = requests.post(url, json=payload)
data = response.json()

print(f"AI Response: {data['ai_response']}")
if data['voice_file_url']:
    print(f"Audio available at: {data['voice_file_url']}")
```

### JavaScript (fetch)

```javascript
const processText = async (text) => {
    const response = await fetch('http://localhost:8000/text/process', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            text: text,
            response_format: 'both'
        })
    });
    
    const data = await response.json();
    console.log('AI Response:', data.ai_response);
    
    if (data.voice_file_url) {
        // Play audio file
        const audio = new Audio(data.voice_file_url);
        audio.play();
    }
};

processText("What is artificial intelligence?");
```

### cURL

```bash
# Voice processing
curl -X POST http://localhost:8000/voice/process \
  -H "Content-Type: application/json" \
  -d '{
    "action": "listen_and_respond",
    "duration": 3,
    "language": "en-US"
  }'

# Text processing
curl -X POST http://localhost:8000/text/process \
  -H "Content-Type: application/json" \
  -d '{
    "text": "Explain machine learning",
    "max_tokens": 100
  }'
```

## WebSocket Support (Future)

Planned WebSocket endpoints for real-time communication:

- `ws://localhost:8000/ws/voice` - Real-time voice streaming
- `ws://localhost:8000/ws/chat` - Live chat interface

## SDKs and Libraries

Official SDKs are planned for:
- Python
- JavaScript/Node.js
- Java
- C#

## Versioning

API versioning will be handled through URL paths:
- Current: `/` (v1 implicit)
- Future: `/v2/`, `/v3/`, etc.

## Support

For API support and questions:
- GitHub Issues: [Voice-GenAI-Tool Issues](https://github.com/VinodHatti7019/Voice-GenAI-Tool/issues)
- Documentation: [Project Wiki](https://github.com/VinodHatti7019/Voice-GenAI-Tool/wiki)

## Changelog

### v1.0.0 (Current)
- Initial API release
- Voice and text processing endpoints
- Health check endpoint
- Configuration management
- Audio file serving

---

*Last updated: October 2024*
