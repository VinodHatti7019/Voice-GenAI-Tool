"""
Configuration Settings for Voice-GenAI-Tool

Author: Vinod Hatti
Version: 1.0.0
Description: Comprehensive configuration management using Pydantic settings
"""

import os
from typing import List, Optional
from pydantic import BaseSettings, Field, validator
from pathlib import Path

class Settings(BaseSettings):
    """Application settings with environment variable support."""
    
    # Application Settings
    APP_NAME: str = Field(default="Voice-GenAI-Tool", description="Application name")
    VERSION: str = Field(default="1.0.0", description="Application version")
    DEBUG: bool = Field(default=False, description="Debug mode")
    HOST: str = Field(default="0.0.0.0", description="Host address")
    PORT: int = Field(default=8000, description="Port number")
    WORKERS: int = Field(default=4, description="Number of workers")
    
    # Security Settings
    SECRET_KEY: str = Field(default="your-secret-key-change-in-production", description="Secret key for JWT")
    ALGORITHM: str = Field(default="HS256", description="JWT algorithm")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = Field(default=30, description="Token expiration time")
    
    # CORS Settings
    ALLOWED_ORIGINS: List[str] = Field(
        default=["http://localhost:3000", "http://localhost:8080", "https://localhost:3000"],
        description="Allowed CORS origins"
    )
    
    # Database Settings
    DATABASE_URL: str = Field(
        default="sqlite+aiosqlite:///./voice_ai.db",
        description="Database connection URL"
    )
    DATABASE_POOL_SIZE: int = Field(default=20, description="Database pool size")
    DATABASE_MAX_OVERFLOW: int = Field(default=30, description="Database max overflow")
    
    # Redis Settings (for caching and session management)
    REDIS_URL: str = Field(default="redis://localhost:6379/0", description="Redis connection URL")
    REDIS_TTL: int = Field(default=3600, description="Redis TTL in seconds")
    
    # AI Model Settings
    OPENAI_API_KEY: Optional[str] = Field(default=None, description="OpenAI API key")
    OPENAI_MODEL: str = Field(default="gpt-3.5-turbo", description="OpenAI model")
    OPENAI_MAX_TOKENS: int = Field(default=1000, description="Max tokens for OpenAI")
    OPENAI_TEMPERATURE: float = Field(default=0.7, description="OpenAI temperature")
    
    # Hugging Face Settings
    HUGGINGFACE_API_KEY: Optional[str] = Field(default=None, description="Hugging Face API key")
    HF_MODEL_NAME: str = Field(default="facebook/wav2vec2-base-960h", description="HuggingFace model")
    
    # Google Cloud Settings
    GOOGLE_CLOUD_PROJECT: Optional[str] = Field(default=None, description="Google Cloud project ID")
    GOOGLE_CLOUD_CREDENTIALS: Optional[str] = Field(default=None, description="Google Cloud credentials")
    
    # Azure Settings
    AZURE_SPEECH_KEY: Optional[str] = Field(default=None, description="Azure Speech API key")
    AZURE_SPEECH_REGION: str = Field(default="eastus", description="Azure Speech region")
    
    # AWS Settings
    AWS_ACCESS_KEY_ID: Optional[str] = Field(default=None, description="AWS access key")
    AWS_SECRET_ACCESS_KEY: Optional[str] = Field(default=None, description="AWS secret key")
    AWS_REGION: str = Field(default="us-east-1", description="AWS region")
    
    # Speech Recognition Settings
    SPEECH_MODEL_TYPE: str = Field(default="whisper", description="Speech recognition model type")
    WHISPER_MODEL_SIZE: str = Field(default="base", description="Whisper model size")
    LANGUAGE_DETECTION: bool = Field(default=True, description="Enable language detection")
    NOISE_REDUCTION: bool = Field(default=True, description="Enable noise reduction")
    
    # Text-to-Speech Settings
    TTS_ENGINE: str = Field(default="gtts", description="TTS engine (gtts, azure, google)")
    DEFAULT_VOICE: str = Field(default="en-US-JennyNeural", description="Default voice")
    SPEECH_SPEED: float = Field(default=1.0, description="Speech speed multiplier")
    AUDIO_FORMAT: str = Field(default="wav", description="Audio output format")
    SAMPLE_RATE: int = Field(default=22050, description="Audio sample rate")
    
    # File Storage Settings
    UPLOAD_DIR: str = Field(default="uploads", description="Upload directory")
    OUTPUT_DIR: str = Field(default="outputs", description="Output directory")
    TEMP_DIR: str = Field(default="temp", description="Temporary files directory")
    MAX_FILE_SIZE: int = Field(default=50 * 1024 * 1024, description="Max file size in bytes (50MB)")
    ALLOWED_AUDIO_FORMATS: List[str] = Field(
        default=["wav", "mp3", "m4a", "flac", "aac", "ogg"],
        description="Allowed audio file formats"
    )
    
    # Logging Settings
    LOG_LEVEL: str = Field(default="INFO", description="Logging level")
    LOG_FILE: str = Field(default="logs/voice_ai.log", description="Log file path")
    LOG_ROTATION: str = Field(default="10 MB", description="Log rotation size")
    LOG_RETENTION: str = Field(default="30 days", description="Log retention period")
    
    # Performance Settings
    MAX_CONCURRENT_REQUESTS: int = Field(default=100, description="Max concurrent requests")
    REQUEST_TIMEOUT: int = Field(default=300, description="Request timeout in seconds")
    AUDIO_PROCESSING_TIMEOUT: int = Field(default=120, description="Audio processing timeout")
    
    # Monitoring Settings
    ENABLE_METRICS: bool = Field(default=True, description="Enable Prometheus metrics")
    METRICS_PORT: int = Field(default=8001, description="Metrics server port")
    HEALTH_CHECK_INTERVAL: int = Field(default=30, description="Health check interval")
    
    # Feature Flags
    ENABLE_VOICE_CLONING: bool = Field(default=False, description="Enable voice cloning feature")
    ENABLE_REAL_TIME_PROCESSING: bool = Field(default=True, description="Enable real-time processing")
    ENABLE_BATCH_PROCESSING: bool = Field(default=True, description="Enable batch processing")
    ENABLE_ANALYTICS: bool = Field(default=True, description="Enable usage analytics")
    
    # Rate Limiting
    RATE_LIMIT_REQUESTS: int = Field(default=100, description="Rate limit per minute")
    RATE_LIMIT_WINDOW: int = Field(default=60, description="Rate limit window in seconds")
    
    # WebSocket Settings
    WS_MAX_CONNECTIONS: int = Field(default=100, description="Max WebSocket connections")
    WS_HEARTBEAT_INTERVAL: int = Field(default=30, description="WebSocket heartbeat interval")
    
    @validator('ALLOWED_ORIGINS', pre=True)
    def parse_origins(cls, v):
        """Parse CORS origins from environment variable."""
        if isinstance(v, str):
            return [origin.strip() for origin in v.split(',')]
        return v
    
    @validator('ALLOWED_AUDIO_FORMATS', pre=True)
    def parse_audio_formats(cls, v):
        """Parse allowed audio formats from environment variable."""
        if isinstance(v, str):
            return [format.strip() for format in v.split(',')]
        return v
    
    @validator('UPLOAD_DIR', 'OUTPUT_DIR', 'TEMP_DIR')
    def create_directories(cls, v):
        """Create directories if they don't exist."""
        Path(v).mkdir(parents=True, exist_ok=True)
        return v
    
    @validator('LOG_FILE')
    def create_log_directory(cls, v):
        """Create log directory if it doesn't exist."""
        log_path = Path(v)
        log_path.parent.mkdir(parents=True, exist_ok=True)
        return v
    
    class Config:
        """Pydantic configuration."""
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True
        validate_assignment = True

# Global settings instance
settings = Settings()

# Configuration validation
def validate_configuration():
    """Validate critical configuration settings."""
    errors = []
    
    # Check required API keys for production
    if not settings.DEBUG:
        if not settings.SECRET_KEY or settings.SECRET_KEY == "your-secret-key-change-in-production":
            errors.append("SECRET_KEY must be set for production")
        
        if not settings.OPENAI_API_KEY and settings.SPEECH_MODEL_TYPE == "openai":
            errors.append("OPENAI_API_KEY required for OpenAI speech models")
    
    # Validate file size limits
    if settings.MAX_FILE_SIZE > 100 * 1024 * 1024:  # 100MB
        errors.append("MAX_FILE_SIZE should not exceed 100MB for optimal performance")
    
    # Validate port ranges
    if not 1024 <= settings.PORT <= 65535:
        errors.append("PORT must be between 1024 and 65535")
    
    if not 1024 <= settings.METRICS_PORT <= 65535:
        errors.append("METRICS_PORT must be between 1024 and 65535")
    
    # Validate timeout settings
    if settings.REQUEST_TIMEOUT < 30:
        errors.append("REQUEST_TIMEOUT should be at least 30 seconds")
    
    if errors:
        raise ValueError(f"Configuration validation failed: {'; '.join(errors)}")

# Environment-specific configurations
class DevelopmentConfig(Settings):
    """Development environment configuration."""
    DEBUG: bool = True
    LOG_LEVEL: str = "DEBUG"
    WORKERS: int = 1

class ProductionConfig(Settings):
    """Production environment configuration."""
    DEBUG: bool = False
    LOG_LEVEL: str = "INFO"
    WORKERS: int = 4
    ENABLE_METRICS: bool = True

class TestingConfig(Settings):
    """Testing environment configuration."""
    DEBUG: bool = True
    DATABASE_URL: str = "sqlite+aiosqlite:///:memory:"
    LOG_LEVEL: str = "WARNING"

# Configuration factory
def get_config(environment: str = None) -> Settings:
    """Get configuration based on environment."""
    environment = environment or os.getenv('ENVIRONMENT', 'development').lower()
    
    config_mapping = {
        'development': DevelopmentConfig,
        'production': ProductionConfig,
        'testing': TestingConfig
    }
    
    config_class = config_mapping.get(environment, Settings)
    config = config_class()
    
    # Validate configuration
    validate_configuration()
    
    return config
