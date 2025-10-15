"""
Voice GenAI Tool - Modules Package

This package contains the core AI/ML modules for voice processing functionality:
- Speech-to-Text (ASR) using Whisper and other models
- Text-to-Speech (TTS) using ElevenLabs and local models
- Voice cloning and synthesis capabilities
- Real-time audio processing pipelines
- Audio preprocessing and postprocessing utilities

Author: VinodHatti7019
Version: 1.0.0
"""

from typing import Dict, Any, Optional, List
import logging
import os
from pathlib import Path

# Package metadata
__version__ = "1.0.0"
__author__ = "VinodHatti7019"
__description__ = "Core AI/ML modules for voice processing in Voice GenAI Tool"

# Initialize logger for the modules package
logger = logging.getLogger(__name__)

# Module configuration constants
MODULE_CONFIG = {
    "version": __version__,
    "supported_models": {
        "asr": ["whisper-tiny", "whisper-base", "whisper-small", "whisper-medium", "whisper-large-v3"],
        "tts": ["elevenlabs", "espeak-ng", "festival", "coqui-tts"],
        "voice_cloning": ["elevenlabs-clone", "so-vits-svc", "real-time-voice-cloning"],
    },
    "supported_languages": [
        "en", "es", "fr", "de", "it", "pt", "ru", "ja", "ko", "zh", 
        "ar", "hi", "tr", "pl", "nl", "sv", "da", "no", "fi"
    ],
    "audio_formats": {
        "input": ["wav", "mp3", "m4a", "flac", "webm", "ogg"],
        "output": ["wav", "mp3", "ogg", "flac"]
    },
    "sample_rates": [16000, 22050, 44100, 48000],
    "default_settings": {
        "sample_rate": 16000,
        "channels": 1,
        "bit_depth": 16,
        "chunk_size": 1024,
        "buffer_size": 4096,
        "max_audio_length": 300,  # seconds
    }
}

# Module paths and directories
MODULE_PATHS = {
    "models_dir": Path("models"),
    "cache_dir": Path("cache"),
    "temp_dir": Path("temp"),
    "audio_dir": Path("audio"),
    "logs_dir": Path("logs"),
}

# Performance settings
PERFORMACE_CONFIG = {
    "use_gpu": True,
    "gpu_memory_fraction": 0.8,
    "num_threads": os.cpu_count(),
    "batch_size": 1,
    "streaming_chunk_size": 1024,
    "realtime_factor": 1.0,
}

def get_module_info() -> Dict[str, Any]:
    """
    Get comprehensive module information.
    
    Returns:
        Dict containing module version, supported models, and configuration
    """
    return {
        "version": __version__,
        "description": __description__,
        "author": __author__,
        "supported_models": MODULE_CONFIG["supported_models"],
        "supported_languages": MODULE_CONFIG["supported_languages"],
        "audio_formats": MODULE_CONFIG["audio_formats"],
        "sample_rates": MODULE_CONFIG["sample_rates"],
        "default_settings": MODULE_CONFIG["default_settings"],
        "performance_config": PERFORME_CONFIG,
        "module_paths": {k: str(v) for k, v in MODULE_PATHS.items()}
    }

def validate_audio_config(config: Dict[str, Any]) -> bool:
    """
    Validate audio processing configuration.
    
    Args:
        config: Audio configuration dictionary
    
    Returns:
        True if configuration is valid, False otherwise
    """
    required_keys = ["sample_rate", "channels", "bit_depth"]
    
    # Check required keys
    for key in required_keys:
        if key not in config:
            logger.error(f"Missing required audio config key: {key}")
            return False
    
    # Validate sample rate
    if config["sample_rate"] not in MODULE_CONFIG["sample_rates"]:
        logger.error(f"Unsupported sample rate: {config['sample_rate']}")
        return False
    
    # Validate channels
    if config["channels"] not in [1, 2]:
        logger.error(f"Unsupported channel count: {config['channels']}")
        return False
    
    # Validate bit depth
    if config["bit_depth"] not in [16, 24, 32]:
        logger.error(f"Unsupported bit depth: {config['bit_depth']}")
        return False
    
    return True

def setup_module_directories() -> bool:
    """
    Create necessary directories for module operation.
    
    Returns:
        True if directories were created successfully, False otherwise
    """
    try:
        for dir_name, dir_path in MODULE_PATHS.items():
            if not dir_path.exists():
                dir_path.mkdir(parents=True, exist_ok=True)
                logger.info(f"Created directory: {dir_path}")
        return True
    except Exception as e:
        logger.error(f"Failed to create module directories: {e}")
        return False

def get_available_models(model_type: str) -> List[str]:
    """
    Get list of available models for a specific type.
    
    Args:
        model_type: Type of model ('asr', 'tts', 'voice_cloning')
    
    Returns:
        List of available model names
    """
    if model_type not in MODULE_CONFIG["supported_models"]:
        logger.warning(f"Unknown model type: {model_type}")
        return []
    
    return MODULE_CONFIG["supported_models"][model_type]

def validate_language_support(language: str) -> bool:
    """
    Check if a language is supported.
    
    Args:
        language: Language code (e.g., 'en', 'es', 'fr')
    
    Returns:
        True if language is supported, False otherwise
    """
    return language.lower() in MODULE_CONFIG["supported_languages"]

def get_default_config(module_type: str) -> Dict[str, Any]:
    """
    Get default configuration for a specific module type.
    
    Args:
        module_type: Type of module ('asr', 'tts', 'voice_cloning')
    
    Returns:
        Default configuration dictionary
    """
    base_config = MODULE_CONFIG["default_settings"].copy()
    base_config.update(PERFORME_CONFIG)
    
    # Module-specific settings
    if module_type == "asr":
        base_config.update({
            "model_name": "whisper-base",
            "language": "auto",
            "task": "transcribe",
            "beam_size": 5,
            "best_of": 5,
            "temperature": 0.0,
        })
    elif module_type == "tts":
        base_config.update({
            "model_name": "elevenlabs",
            "voice_id": "default",
            "stability": 0.75,
            "similarity_boost": 0.75,
            "style": 0.0,
            "use_speaker_boost": True,
        })
    elif module_type == "voice_cloning":
        base_config.update({
            "model_name": "elevenlabs-clone",
            "similarity_threshold": 0.8,
            "quality": "high",
            "preserve_accent": True,
        })
    
    return base_config

# Initialize module directories on import
setup_module_directories()

# Log module initialization
logger.info(f"Voice GenAI Tool modules package initialized (v{__version__})")
logger.info(f"Supported ASR models: {MODULE_CONFIG['supported_models']['asr']}")
logger.info(f"Supported TTS models: {MODULE_CONFIG['supported_models']['tts']}")
logger.info(f"Supported languages: {len(MODULE_CONFIG['supported_languages'])} languages")
logger.info(f"Module directories: {list(MODULE_PATHS.keys())}")

# Export main components
__all__ = [
    "__version__",
    "__author__",
    "__description__",
    "MODULE_CONFIG",
    "MODULE_PATHS",
    "PERFORME_CONFIG",
    "get_module_info",
    "validate_audio_config",
    "setup_module_directories",
    "get_available_models",
    "validate_language_support",
    "get_default_config",
]
