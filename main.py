#!/usr/bin/env python3
"""
Voice GenAI Tool - Main Entry Point

This is the main entry point for the Voice GenAI Tool application.
It provides a comprehensive voice-powered AI interface with support for:
- Speech-to-Text (ASR)
- Text-to-Speech (TTS)
- AI-powered conversation
- Voice command processing

Author: VinodHatti7019
Version: 1.0.0
"""

import sys
import os
import asyncio
import argparse
from pathlib import Path

# Add src directory to Python path
project_root = Path(__file__).parent
src_path = project_root / "src"
if src_path.exists():
    sys.path.insert(0, str(src_path))

try:
    import uvicorn
    from app import app
    from utils.logger import get_logger
    from utils.config import load_config
except ImportError as e:
    print(f"Error importing required modules: {e}")
    print("Please ensure all dependencies are installed: pip install -r requirements.txt")
    sys.exit(1)

# Initialize logger
logger = get_logger(__name__)

def parse_arguments():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="Voice GenAI Tool - AI-powered voice assistant"
    )
    parser.add_argument(
        "--host",
        type=str,
        default="0.0.0.0",
        help="Host to bind the server to (default: 0.0.0.0)"
    )
    parser.add_argument(
        "--port",
        type=int,
        default=8000,
        help="Port to bind the server to (default: 8000)"
    )
    parser.add_argument(
        "--reload",
        action="store_true",
        help="Enable auto-reload for development"
    )
    parser.add_argument(
        "--workers",
        type=int,
        default=1,
        help="Number of worker processes (default: 1)"
    )
    parser.add_argument(
        "--log-level",
        type=str,
        default="info",
        choices=["debug", "info", "warning", "error", "critical"],
        help="Logging level (default: info)"
    )
    parser.add_argument(
        "--config",
        type=str,
        help="Path to configuration file"
    )
    return parser.parse_args()

def validate_environment():
    """Validate that the environment is properly configured."""
    logger.info("Validating environment...")
    
    # Check for required directories
    required_dirs = ["src", "src/utils"]
    for dir_path in required_dirs:
        if not Path(dir_path).exists():
            logger.error(f"Required directory '{dir_path}' not found")
            return False
    
    # Check for required files
    required_files = ["app.py", "requirements.txt", "src/utils/config.py", "src/utils/logger.py"]
    for file_path in required_files:
        if not Path(file_path).exists():
            logger.error(f"Required file '{file_path}' not found")
            return False
    
    logger.info("Environment validation passed")
    return True

def setup_logging(log_level: str):
    """Setup logging configuration."""
    import logging
    
    # Configure root logger
    logging.basicConfig(
        level=getattr(logging, log_level.upper()),
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[
            logging.StreamHandler(sys.stdout),
            logging.FileHandler("voice_genai_tool.log")
        ]
    )

async def startup_checks():
    """Perform startup checks and initialization."""
    logger.info("Performing startup checks...")
    
    try:
        # Load and validate configuration
        config = load_config()
        logger.info("Configuration loaded successfully")
        
        # Perform any additional startup tasks here
        # e.g., model loading, API key validation, etc.
        
        logger.info("Startup checks completed successfully")
        return True
        
    except Exception as e:
        logger.error(f"Startup checks failed: {e}")
        return False

def main():
    """Main entry point for the Voice GenAI Tool application."""
    try:
        # Parse command line arguments
        args = parse_arguments()
        
        # Setup logging
        setup_logging(args.log_level)
        
        logger.info("Starting Voice GenAI Tool...")
        logger.info(f"Python version: {sys.version}")
        logger.info(f"Working directory: {os.getcwd()}")
        
        # Validate environment
        if not validate_environment():
            logger.error("Environment validation failed")
            sys.exit(1)
        
        # Perform startup checks
        if not asyncio.run(startup_checks()):
            logger.error("Startup checks failed")
            sys.exit(1)
        
        # Start the FastAPI server
        logger.info(f"Starting server on {args.host}:{args.port}")
        
        uvicorn_config = {
            "app": "app:app",
            "host": args.host,
            "port": args.port,
            "log_level": args.log_level,
            "access_log": True,
        }
        
        if args.reload:
            uvicorn_config["reload"] = True
            logger.info("Auto-reload enabled for development")
        else:
            uvicorn_config["workers"] = args.workers
            if args.workers > 1:
                logger.info(f"Starting with {args.workers} worker processes")
        
        # Run the server
        uvicorn.run(**uvicorn_config)
        
    except KeyboardInterrupt:
        logger.info("Received interrupt signal, shutting down gracefully...")
    except Exception as e:
        logger.error(f"An error occurred: {e}")
        sys.exit(1)
    finally:
        logger.info("Voice GenAI Tool shutdown complete")

if __name__ == "__main__":
    main()
