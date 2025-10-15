"""
Voice GenAI Tool - API Module

This package contains the API endpoints and routing logic for the Voice GenAI Tool.
It provides RESTful API interfaces for:
- Speech-to-Text (ASR) functionality
- Text-to-Speech (TTS) functionality
- AI conversation endpoints
- Voice command processing
- Real-time voice streaming

Author: VinodHatti7019
Version: 1.0.0
"""

from typing import Dict, Any
import logging

# Package version
__version__ = "1.0.0"

# Package author
__author__ = "VinodHatti7019"

# Package description
__description__ = "API module for Voice GenAI Tool - Provides RESTful endpoints for voice AI functionality"

# Initialize logger for the API module
logger = logging.getLogger(__name__)

# API configuration constants
API_CONFIG = {
    "version": __version__,
    "title": "Voice GenAI Tool API",
    "description": __description__,
    "contact": {
        "name": "VinodHatti7019",
        "url": "https://github.com/VinodHatti7019/Voice-GenAI-Tool",
    },
    "license": {
        "name": "MIT",
        "url": "https://opensource.org/licenses/MIT",
    },
}

# API endpoint prefixes
API_PREFIXES = {
    "speech": "/api/v1/speech",
    "tts": "/api/v1/tts",
    "conversation": "/api/v1/conversation",
    "health": "/api/v1/health",
    "websocket": "/ws",
}

# Supported audio formats
SUPPORTED_AUDIO_FORMATS = {
    "input": ["wav", "mp3", "m4a", "flac", "webm"],
    "output": ["wav", "mp3", "ogg"]
}

# Default API settings
DEFAULT_SETTINGS = {
    "max_file_size": 50 * 1024 * 1024,  # 50MB
    "timeout": 30,  # seconds
    "rate_limit": {
        "requests_per_minute": 60,
        "requests_per_hour": 1000,
    },
}

def get_api_info() -> Dict[str, Any]:
    """
    Get comprehensive API information.
    
    Returns:
        Dict containing API version, endpoints, and configuration info
    """
    return {
        "api_version": __version__,
        "title": API_CONFIG["title"],
        "description": API_CONFIG["description"],
        "endpoints": API_PREFIXES,
        "supported_formats": SUPPORTED_AUDIO_FORMATS,
        "settings": DEFAULT_SETTINGS,
        "contact": API_CONFIG["contact"],
        "license": API_CONFIG["license"],
    }

def validate_audio_format(file_format: str, format_type: str = "input") -> bool:
    """
    Validate if the audio format is supported.
    
    Args:
        file_format: Audio file format (e.g., 'wav', 'mp3')
        format_type: Type of format validation ('input' or 'output')
    
    Returns:
        True if format is supported, False otherwise
    """
    if format_type not in SUPPORTED_AUDIO_FORMATS:
        return False
    
    return file_format.lower() in SUPPORTED_AUDIO_FORMATS[format_type]

def get_endpoint_url(endpoint_type: str, base_url: str = "") -> str:
    """
    Get the full URL for a specific API endpoint.
    
    Args:
        endpoint_type: Type of endpoint (e.g., 'speech', 'tts', 'conversation')
        base_url: Base URL for the API server
    
    Returns:
        Full endpoint URL
    """
    if endpoint_type not in API_PREFIXES:
        raise ValueError(f"Unknown endpoint type: {endpoint_type}")
    
    prefix = API_PREFIXES[endpoint_type]
    return f"{base_url.rstrip('/')}{prefix}" if base_url else prefix

# Log module initialization
logger.info(f"Voice GenAI Tool API module initialized (v{__version__})")
logger.info(f"Available endpoints: {list(API_PREFIXES.keys())}")
logger.info(f"Supported input formats: {SUPPORTED_AUDIO_FORMATS['input']}")
logger.info(f"Supported output formats: {SUPPORTED_AUDIO_FORMATS['output']}")

# Export main components
__all__ = [
    "__version__",
    "__author__",
    "__description__",
    "API_CONFIG",
    "API_PREFIXES",
    "SUPPORTED_AUDIO_FORMATS",
    "DEFAULT_SETTINGS",
    "get_api_info",
    "validate_audio_format",
    "get_endpoint_url",
]
