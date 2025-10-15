"""
Advanced Logging Configuration for Voice-GenAI-Tool

Author: Vinod Hatti
Version: 1.0.0
Description: Production-ready logging setup with Loguru and structured logging
"""

import os
import sys
from pathlib import Path
from typing import Dict, Any, Optional
from loguru import logger
from datetime import datetime
import json

def setup_logging(
    log_level: str = "INFO",
    log_file: str = "logs/voice_ai.log",
    log_rotation: str = "10 MB",
    log_retention: str = "30 days",
    enable_json: bool = False
) -> None:
    """Setup comprehensive logging configuration."""
    
    # Remove default logger
    logger.remove()
    
    # Create logs directory if it doesn't exist
    log_path = Path(log_file)
    log_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Console logging format
    console_format = (
        "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
        "<level>{level: <8}</level> | "
        "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> | "
        "<level>{message}</level>"
    )
    
    # File logging format
    file_format = (
        "{time:YYYY-MM-DD HH:mm:ss.SSS} | "
        "{level: <8} | "
        "{name}:{function}:{line} | "
        "{message}"
    )
    
    # JSON format for structured logging
    def json_formatter(record):
        """Format log records as JSON."""
        log_record = {
            "timestamp": record["time"].isoformat(),
            "level": record["level"].name,
            "module": record["name"],
            "function": record["function"],
            "line": record["line"],
            "message": record["message"]
        }
        
        # Add extra fields if present
        if record["extra"]:
            log_record.update(record["extra"])
            
        return json.dumps(log_record)
    
    # Console handler
    logger.add(
        sys.stderr,
        format=console_format,
        level=log_level,
        colorize=True,
        backtrace=True,
        diagnose=True,
        enqueue=True
    )
    
    # File handler (standard format)
    logger.add(
        log_file,
        format=file_format if not enable_json else json_formatter,
        level=log_level,
        rotation=log_rotation,
        retention=log_retention,
        compression="zip",
        backtrace=True,
        diagnose=True,
        enqueue=True
    )
    
    # Separate error log file
    error_log_file = log_file.replace(".log", "_error.log")
    logger.add(
        error_log_file,
        format=file_format if not enable_json else json_formatter,
        level="ERROR",
        rotation=log_rotation,
        retention=log_retention,
        compression="zip",
        backtrace=True,
        diagnose=True,
        enqueue=True
    )
    
    # Performance log file for metrics
    performance_log_file = log_file.replace(".log", "_performance.log")
    logger.add(
        performance_log_file,
        format=json_formatter,
        level="INFO",
        rotation="1 day",
        retention="7 days",
        compression="zip",
        filter=lambda record: "performance" in record["extra"],
        enqueue=True
    )
    
    logger.info(f"Logging initialized - Level: {log_level}, File: {log_file}")

class PerformanceLogger:
    """Logger for performance metrics and timing."""
    
    def __init__(self, operation_name: str):
        self.operation_name = operation_name
        self.start_time = None
        self.metadata = {}
    
    def __enter__(self):
        self.start_time = datetime.utcnow()
        logger.info(f"Starting operation: {self.operation_name}", performance=True)
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        end_time = datetime.utcnow()
        duration = (end_time - self.start_time).total_seconds()
        
        log_data = {
            "performance": True,
            "operation": self.operation_name,
            "duration_seconds": duration,
            "start_time": self.start_time.isoformat(),
            "end_time": end_time.isoformat(),
            "success": exc_type is None,
            **self.metadata
        }
        
        if exc_type:
            log_data["error_type"] = exc_type.__name__
            log_data["error_message"] = str(exc_val)
        
        logger.info(
            f"Operation {self.operation_name} completed in {duration:.3f}s",
            **log_data
        )
    
    def add_metadata(self, **kwargs):
        """Add metadata to the performance log."""
        self.metadata.update(kwargs)

class APILogger:
    """Logger for API requests and responses."""
    
    @staticmethod
    def log_request(request_id: str, method: str, path: str, params: Dict = None):
        """Log API request details."""
        logger.info(
            f"API Request: {method} {path}",
            api_request=True,
            request_id=request_id,
            method=method,
            path=path,
            params=params or {}
        )
    
    @staticmethod
    def log_response(
        request_id: str, 
        status_code: int, 
        duration: float,
        response_size: Optional[int] = None
    ):
        """Log API response details."""
        logger.info(
            f"API Response: {status_code} ({duration:.3f}s)",
            api_response=True,
            request_id=request_id,
            status_code=status_code,
            duration=duration,
            response_size=response_size
        )
    
    @staticmethod
    def log_error(request_id: str, error: Exception, context: Dict = None):
        """Log API error details."""
        logger.error(
            f"API Error: {type(error).__name__}: {str(error)}",
            api_error=True,
            request_id=request_id,
            error_type=type(error).__name__,
            error_message=str(error),
            context=context or {}
        )

class AudioProcessingLogger:
    """Specialized logger for audio processing operations."""
    
    @staticmethod
    def log_audio_upload(filename: str, file_size: int, content_type: str):
        """Log audio file upload."""
        logger.info(
            f"Audio uploaded: {filename} ({file_size} bytes)",
            audio_upload=True,
            filename=filename,
            file_size=file_size,
            content_type=content_type
        )
    
    @staticmethod
    def log_transcription(
        filename: str, 
        duration: float, 
        text_length: int,
        confidence: float,
        model_used: str
    ):
        """Log speech-to-text transcription."""
        logger.info(
            f"Transcription completed: {filename} -> {text_length} chars",
            transcription=True,
            filename=filename,
            audio_duration=duration,
            text_length=text_length,
            confidence=confidence,
            model_used=model_used
        )
    
    @staticmethod
    def log_synthesis(
        text_length: int,
        audio_duration: float,
        voice: str,
        language: str
    ):
        """Log text-to-speech synthesis."""
        logger.info(
            f"Speech synthesis: {text_length} chars -> {audio_duration:.2f}s audio",
            synthesis=True,
            text_length=text_length,
            audio_duration=audio_duration,
            voice=voice,
            language=language
        )

class AIModelLogger:
    """Logger for AI model interactions."""
    
    @staticmethod
    def log_model_request(
        model_name: str,
        input_tokens: int,
        parameters: Dict[str, Any]
    ):
        """Log AI model request."""
        logger.info(
            f"AI Model Request: {model_name} ({input_tokens} tokens)",
            ai_model_request=True,
            model_name=model_name,
            input_tokens=input_tokens,
            parameters=parameters
        )
    
    @staticmethod
    def log_model_response(
        model_name: str,
        output_tokens: int,
        duration: float,
        cost: Optional[float] = None
    ):
        """Log AI model response."""
        logger.info(
            f"AI Model Response: {model_name} -> {output_tokens} tokens ({duration:.3f}s)",
            ai_model_response=True,
            model_name=model_name,
            output_tokens=output_tokens,
            duration=duration,
            cost=cost
        )

# Convenience functions for common logging patterns
def log_performance(operation_name: str):
    """Decorator for performance logging."""
    def decorator(func):
        def wrapper(*args, **kwargs):
            with PerformanceLogger(operation_name) as perf:
                perf.add_metadata(function_name=func.__name__)
                return func(*args, **kwargs)
        return wrapper
    return decorator

def log_errors(operation_name: str):
    """Decorator for error logging."""
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                logger.error(
                    f"Error in {operation_name}: {type(e).__name__}: {str(e)}",
                    operation=operation_name,
                    function_name=func.__name__,
                    error_type=type(e).__name__,
                    error_message=str(e)
                )
                raise
        return wrapper
    return decorator

# Initialize structured logging context
def init_request_context(request_id: str, user_id: str = None):
    """Initialize logging context for a request."""
    context = {
        "request_id": request_id,
        "user_id": user_id,
        "timestamp": datetime.utcnow().isoformat()
    }
    
    # Bind context to logger
    return logger.bind(**context)

# Health check logging
def log_health_check(service: str, status: str, details: Dict[str, Any] = None):
    """Log health check results."""
    logger.info(
        f"Health Check: {service} - {status}",
        health_check=True,
        service=service,
        status=status,
        details=details or {}
    )

# Security event logging
def log_security_event(event_type: str, details: Dict[str, Any]):
    """Log security-related events."""
    logger.warning(
        f"Security Event: {event_type}",
        security_event=True,
        event_type=event_type,
        **details
    )

# Export commonly used loggers
api_logger = APILogger()
audio_logger = AudioProcessingLogger()
ai_logger = AIModelLogger()

# Configure logger based on environment
if __name__ == "__main__":
    # Example setup for different environments
    environment = os.getenv('ENVIRONMENT', 'development').lower()
    
    if environment == 'production':
        setup_logging(
            log_level="INFO",
            log_file="logs/production.log",
            enable_json=True
        )
    elif environment == 'development':
        setup_logging(
            log_level="DEBUG",
            log_file="logs/development.log",
            enable_json=False
        )
    else:
        setup_logging()
    
    logger.info(f"Logging configured for {environment} environment")
