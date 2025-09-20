from gettext import npgettext
import pytest # type: ignore
import streamlit as st
from utils.ai_models import XRayClassifier, VoiceProcessor # type: ignore

def test_xray_classifier():
    classifier = XRayClassifier()
    # Test with dummy image
    dummy_image = npgettext.zeros((224, 224, 3))
    result = classifier.predict(dummy_image)
    
    assert "condition" in result
    assert "confidence" in result
    assert result["confidence"] > 0

def test_voice_processor():
    processor = VoiceProcessor()
    result = processor.transcribe(None)  # Dummy audio
    
    assert isinstance(result, str)
    assert len(result) > 0
