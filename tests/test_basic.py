"""Basic health check tests for Voice-GenAI-Tool."""
import pytest
import sys
from pathlib import Path
from fastapi.testclient import TestClient

def test_python_version():
    """Test that Python version is 3.8 or higher."""
    assert sys.version_info >= (3, 8), "Python 3.8+ is required"

def test_project_structure():
    """Test that essential project files exist."""
    project_root = Path(__file__).parent.parent
    assert (project_root / "README.md").exists(), "README.md should exist"
    assert (project_root / "requirements.txt").exists(), "requirements.txt should exist"

def test_imports():
    """Test that key dependencies can be imported."""
    try:
        import speech_recognition
        import pyttsx3
        import openai
        assert True
    except ImportError as e:
        pytest.fail(f"Failed to import required dependency: {e}")

def test_health_endpoint():
    """Test that /health endpoint exists and returns 200 OK."""
    try:
        from main import app
        client = TestClient(app)
        response = client.get("/health")
        assert response.status_code == 200
        assert "status" in response.json()
    except ImportError as e:
        pytest.fail(f"Failed to import main app: {e}")

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
