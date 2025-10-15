"""
Voice-GenAI-Tool: Advanced Voice AI Processing Tool
Main FastAPI Application

Author: Vinod Hatti
Version: 1.0.0
Description: Production-ready voice AI tool with speech-to-text, text-to-speech,
             and AI-powered conversation capabilities.
"""

import os
import asyncio
from typing import Optional, Dict, Any, List
from pathlib import Path

from fastapi import FastAPI, HTTPException, UploadFile, File, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse, FileResponse
from pydantic import BaseModel
from loguru import logger
import uvicorn

from src.audio.speech_processor import SpeechProcessor
from src.ai.conversation_engine import ConversationEngine
from src.utils.config import Settings
from src.utils.logger import setup_logging
from src.database.session import get_db_session
from src.api.models import (
    VoiceRequest,
    VoiceResponse,
    ConversationRequest,
    ConversationResponse,
    AudioUploadResponse
)

# Initialize settings and logging
settings = Settings()
setup_logging(settings.LOG_LEVEL)

# Initialize FastAPI app
app = FastAPI(
    title="Voice-GenAI-Tool",
    description="Advanced Voice AI Processing Tool with Speech Recognition and Generation",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static files
static_dir = Path("static")
static_dir.mkdir(exist_ok=True)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Initialize core components
speech_processor = SpeechProcessor(settings)
conversation_engine = ConversationEngine(settings)

@app.on_event("startup")
async def startup_event():
    """Initialize application components on startup."""
    logger.info("Starting Voice-GenAI-Tool application...")
    
    # Initialize database
    await init_database()
    
    # Initialize AI models
    await conversation_engine.initialize()
    await speech_processor.initialize()
    
    logger.info("Application startup completed successfully")

@app.on_event("shutdown")
async def shutdown_event():
    """Cleanup on application shutdown."""
    logger.info("Shutting down Voice-GenAI-Tool application...")
    
    await conversation_engine.cleanup()
    await speech_processor.cleanup()
    
    logger.info("Application shutdown completed")

async def init_database():
    """Initialize database connection and tables."""
    try:
        async with get_db_session() as session:
            logger.info("Database connection established")
    except Exception as e:
        logger.error(f"Database initialization failed: {e}")
        raise

@app.get("/")
async def root():
    """Root endpoint with API information."""
    return {
        "message": "Welcome to Voice-GenAI-Tool API",
        "version": "1.0.0",
        "docs": "/docs",
        "status": "active"
    }

@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {
        "status": "healthy",
        "timestamp": asyncio.get_event_loop().time(),
        "services": {
            "speech_processor": await speech_processor.health_check(),
            "conversation_engine": await conversation_engine.health_check()
        }
    }

@app.post("/api/v1/speech-to-text", response_model=VoiceResponse)
async def speech_to_text(
    background_tasks: BackgroundTasks,
    audio_file: UploadFile = File(..., description="Audio file for transcription")
):
    """Convert speech to text using advanced ASR models."""
    try:
        logger.info(f"Processing speech-to-text request: {audio_file.filename}")
        
        # Validate audio file
        if not audio_file.content_type.startswith('audio/'):
            raise HTTPException(status_code=400, detail="Invalid audio file format")
        
        # Process audio file
        result = await speech_processor.transcribe_audio(audio_file)
        
        # Add background task for analytics
        background_tasks.add_task(
            log_usage_analytics, 
            "speech-to-text", 
            audio_file.filename,
            result.get("confidence", 0)
        )
        
        return VoiceResponse(
            text=result["text"],
            confidence=result["confidence"],
            processing_time=result["processing_time"],
            language=result.get("language", "auto-detected")
        )
        
    except Exception as e:
        logger.error(f"Speech-to-text processing failed: {e}")
        raise HTTPException(status_code=500, detail=f"Processing failed: {str(e)}")

@app.post("/api/v1/text-to-speech", response_class=FileResponse)
async def text_to_speech(
    request: VoiceRequest,
    background_tasks: BackgroundTasks
):
    """Convert text to speech using advanced TTS models."""
    try:
        logger.info(f"Processing text-to-speech request: {request.text[:50]}...")
        
        # Generate speech from text
        audio_file_path = await speech_processor.synthesize_speech(
            text=request.text,
            voice=request.voice or "default",
            language=request.language or "en",
            speed=request.speed or 1.0
        )
        
        # Add background task for cleanup
        background_tasks.add_task(cleanup_temp_file, audio_file_path)
        
        return FileResponse(
            path=audio_file_path,
            media_type="audio/wav",
            filename=f"speech_{asyncio.get_event_loop().time()}.wav"
        )
        
    except Exception as e:
        logger.error(f"Text-to-speech processing failed: {e}")
        raise HTTPException(status_code=500, detail=f"Processing failed: {str(e)}")

@app.post("/api/v1/conversation", response_model=ConversationResponse)
async def ai_conversation(
    request: ConversationRequest,
    background_tasks: BackgroundTasks
):
    """Process AI-powered conversation with context awareness."""
    try:
        logger.info(f"Processing conversation request: {request.message[:50]}...")
        
        # Process conversation with AI engine
        response = await conversation_engine.process_conversation(
            message=request.message,
            context=request.context,
            user_id=request.user_id,
            conversation_id=request.conversation_id
        )
        
        # Add background task for conversation logging
        background_tasks.add_task(
            log_conversation,
            request.user_id,
            request.message,
            response["response"]
        )
        
        return ConversationResponse(
            response=response["response"],
            context=response["context"],
            conversation_id=response["conversation_id"],
            confidence=response.get("confidence", 0.95),
            processing_time=response["processing_time"]
        )
        
    except Exception as e:
        logger.error(f"Conversation processing failed: {e}")
        raise HTTPException(status_code=500, detail=f"Processing failed: {str(e)}")

@app.post("/api/v1/voice-conversation")
async def voice_conversation(
    background_tasks: BackgroundTasks,
    audio_file: UploadFile = File(..., description="Voice message for AI conversation")
):
    """End-to-end voice conversation: speech-to-text, AI processing, text-to-speech."""
    try:
        logger.info(f"Processing voice conversation: {audio_file.filename}")
        
        # Step 1: Speech to Text
        transcription = await speech_processor.transcribe_audio(audio_file)
        
        # Step 2: AI Conversation
        conversation_response = await conversation_engine.process_conversation(
            message=transcription["text"],
            context={},
            user_id="voice_user"
        )
        
        # Step 3: Text to Speech
        audio_response_path = await speech_processor.synthesize_speech(
            text=conversation_response["response"],
            voice="default",
            language="en"
        )
        
        # Add cleanup background task
        background_tasks.add_task(cleanup_temp_file, audio_response_path)
        
        return {
            "transcription": transcription["text"],
            "ai_response": conversation_response["response"],
            "audio_url": f"/static/audio/{Path(audio_response_path).name}",
            "processing_time": {
                "transcription": transcription["processing_time"],
                "ai_processing": conversation_response["processing_time"]
            }
        }
        
    except Exception as e:
        logger.error(f"Voice conversation processing failed: {e}")
        raise HTTPException(status_code=500, detail=f"Processing failed: {str(e)}")

@app.get("/api/v1/models")
async def list_available_models():
    """List all available AI and speech models."""
    return {
        "speech_models": await speech_processor.list_models(),
        "ai_models": await conversation_engine.list_models(),
        "voices": await speech_processor.list_voices()
    }

@app.get("/api/v1/stats")
async def get_usage_statistics():
    """Get usage statistics and analytics."""
    try:
        async with get_db_session() as session:
            stats = await get_analytics_data(session)
            return stats
    except Exception as e:
        logger.error(f"Failed to fetch statistics: {e}")
        raise HTTPException(status_code=500, detail="Failed to fetch statistics")

# Background task functions
async def log_usage_analytics(service: str, filename: str, confidence: float):
    """Log usage analytics to database."""
    try:
        async with get_db_session() as session:
            await save_analytics(session, service, filename, confidence)
    except Exception as e:
        logger.error(f"Analytics logging failed: {e}")

async def log_conversation(user_id: str, input_message: str, response: str):
    """Log conversation to database for analytics."""
    try:
        async with get_db_session() as session:
            await save_conversation_log(session, user_id, input_message, response)
    except Exception as e:
        logger.error(f"Conversation logging failed: {e}")

async def cleanup_temp_file(file_path: str):
    """Clean up temporary files after use."""
    try:
        await asyncio.sleep(300)  # Wait 5 minutes before cleanup
        if os.path.exists(file_path):
            os.remove(file_path)
            logger.info(f"Cleaned up temporary file: {file_path}")
    except Exception as e:
        logger.error(f"File cleanup failed: {e}")

if __name__ == "__main__":
    uvicorn.run(
        "app:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.DEBUG,
        workers=settings.WORKERS if not settings.DEBUG else 1,
        log_config=None,  # Use custom logging
        access_log=False  # Disable default access log
    )
