from fastapi import APIRouter, HTTPException, status
from app.schemas.code import CodeAnalysis, CodeGeneration
from app.services.ai_service import ai_service
from typing import List

router = APIRouter()

@router.post("/analyze", response_model=CodeAnalysis)
async def analyze_code(code: str):
    """Analyze code and provide insights"""
    return await ai_service.analyze(code)

@router.post("/generate", response_model=CodeGeneration)
async def generate_code(prompt: str):
    """Generate code from prompt"""
    return await ai_service.generate(prompt)

@router.get("/health")
async def health_check():
    return {"status": "healthy"}
