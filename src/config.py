"""Configuration management for Voice GenAI Tool.

Loads environment variables and provides configuration settings
for the backend API, including CORS, logging, and service settings.
"""

import os
from pathlib import Path
from typing import List, Optional
from pydantic import BaseSettings, validator
from dotenv import load_dotenv

# Load environment variables from .env file
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""
    
    # API Keys
    elevenlabs_api_key: Optional[str] = os.getenv('ELEVENLABS_API_KEY')
    openai_api_key: Optional[str] = os.getenv('OPENAI_API_KEY')
    google_cloud_api_key: Optional[str] = os.getenv('GOOGLE_CLOUD_API_KEY')
    
    # Server Configuration
    api_host: str = os.getenv('API_HOST', '0.0.0.0')
    api_port: int = int(os.getenv('API_PORT', '8000'))
    environment: str = os.getenv('ENVIRONMENT', 'development')
    debug: bool = os.getenv('DEBUG', 'True').lower() == 'true'
    
    # CORS Configuration
    cors_origins: List[str] = [
        origin.strip() 
        for origin in os.getenv('CORS_ORIGINS', 'http://localhost:80,http://localhost:3000').split(',')
    ]
    allow_credentials: bool = os.getenv('ALLOW_CREDENTIALS', 'True').lower() == 'true'
    allow_methods: List[str] = os.getenv('ALLOW_METHODS', '*').split(',')
    allow_headers: List[str] = os.getenv('ALLOW_HEADERS', '*').split(',')
    
    # Logging
    log_level: str = os.getenv('LOG_LEVEL', 'info').upper()
    log_file: str = os.getenv('LOG_FILE', 'logs/voice-genai.log')
    
    # Model Paths
    model_dir: Path = Path(os.getenv('MODEL_DIR', './models'))
    data_dir: Path = Path(os.getenv('DATA_DIR', './data'))
    cache_dir: Path = Path(os.getenv('CACHE_DIR', './cache'))
    
    # Voice Processing Settings
    sample_rate: int = int(os.getenv('SAMPLE_RATE', '16000'))
    max_audio_length: int = int(os.getenv('MAX_AUDIO_LENGTH', '300'))
    audio_format: str = os.getenv('AUDIO_FORMAT', 'wav')
    
    # Language Support
    default_language: str = os.getenv('DEFAULT_LANGUAGE', 'en')
    supported_languages: List[str] = [
        lang.strip()
        for lang in os.getenv('SUPPORTED_LANGUAGES', 'en,es,fr,de,hi,zh,ja,ar,ru,pt').split(',')
    ]
    
    # Performance Settings
    max_concurrent_requests: int = int(os.getenv('MAX_CONCURRENT_REQUESTS', '10'))
    request_timeout: int = int(os.getenv('REQUEST_TIMEOUT', '30'))
    cache_enabled: bool = os.getenv('CACHE_ENABLED', 'True').lower() == 'true'
    cache_ttl: int = int(os.getenv('CACHE_TTL', '3600'))
    
    # Database (optional)
    database_url: str = os.getenv('DATABASE_URL', 'sqlite:///./voice_genai.db')
    database_echo: bool = os.getenv('DATABASE_ECHO', 'False').lower() == 'true'
    
    # Redis (optional)
    redis_host: str = os.getenv('REDIS_HOST', 'localhost')
    redis_port: int = int(os.getenv('REDIS_PORT', '6379'))
    redis_db: int = int(os.getenv('REDIS_DB', '0'))
    
    # Security
    secret_key: str = os.getenv('SECRET_KEY', 'default_secret_key_change_in_production')
    api_key_header: str = os.getenv('API_KEY_HEADER', 'X-API-Key')
    rate_limit_enabled: bool = os.getenv('RATE_LIMIT_ENABLED', 'True').lower() == 'true'
    rate_limit_per_minute: int = int(os.getenv('RATE_LIMIT_PER_MINUTE', '60'))
    
    @validator('model_dir', 'data_dir', 'cache_dir')
    def create_directories(cls, v: Path) -> Path:
        """Ensure directories exist."""
        v.mkdir(parents=True, exist_ok=True)
        return v
    
    @property
    def is_production(self) -> bool:
        """Check if running in production environment."""
        return self.environment.lower() == 'production'
    
    @property
    def is_development(self) -> bool:
        """Check if running in development environment."""
        return self.environment.lower() == 'development'
    
    class Config:
        """Pydantic configuration."""
        case_sensitive = False
        env_file = '.env'
        env_file_encoding = 'utf-8'


# Global settings instance
settings = Settings()


def get_settings() -> Settings:
    """Get application settings.
    
    Returns:
        Settings: Application configuration settings
    """
    return settings


def get_cors_config() -> dict:
    """Get CORS configuration for FastAPI.
    
    Returns:
        dict: CORS configuration dictionary
    """
    return {
        'allow_origins': settings.cors_origins,
        'allow_credentials': settings.allow_credentials,
        'allow_methods': settings.allow_methods,
        'allow_headers': settings.allow_headers,
    }


def get_api_info() -> dict:
    """Get API information.
    
    Returns:
        dict: API information dictionary
    """
    return {
        'title': 'Voice GenAI Tool API',
        'description': 'Multilingual Voice AI with Speech Recognition, TTS & Voice Cloning',
        'version': '1.0.0',
        'contact': {
            'name': 'Voice GenAI Team',
            'url': 'https://github.com/VinodHatti7019/Voice-GenAI-Tool',
        },
        'license_info': {
            'name': 'MIT',
        },
    }
