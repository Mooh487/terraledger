"""
LLM API router for TerraLedger Carbon Exchange.
Provides AI-powered analysis and content generation for carbon credits.
"""
from fastapi import APIRouter, HTTPException, Body
from typing import Dict, Any, Optional, List
from pydantic import BaseModel
from ...services.llm_service import LLMService
import logging

# Configure logging
logger = logging.getLogger(__name__)

# Create router
router = APIRouter()

# Initialize LLM service
llm_service = LLMService()

# Pydantic models for request/response
class LLMRequest(BaseModel):
    prompt: str
    system_message: Optional[str] = None
    conversation_history: Optional[List[Dict[str, str]]] = None
    model: Optional[str] = None
    temperature: float = 0.7
    max_tokens: int = 1024

class CarbonProjectAnalysisRequest(BaseModel):
    project_data: Dict[str, Any]

class SatelliteImageryRequest(BaseModel):
    image_description: str
    location_data: Dict[str, Any]
    historical_data: Optional[List[Dict[str, Any]]] = None

class CreditDescriptionRequest(BaseModel):
    credit_data: Dict[str, Any]

@router.post("/generate")
async def generate_response(request: LLMRequest):
    """
    Generate a response from the LLM using Groq API.
    """
    try:
        result = llm_service.generate_response(
            prompt=request.prompt,
            system_message=request.system_message,
            conversation_history=request.conversation_history,
            model=request.model,
            temperature=request.temperature,
            max_tokens=request.max_tokens
        )
        
        if not result.get("success", False):
            raise HTTPException(status_code=400, detail=result.get("error", "Failed to generate response"))
        
        return result
        
    except Exception as e:
        logger.error(f"Error generating LLM response: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/analyze-carbon-project")
async def analyze_carbon_project(request: CarbonProjectAnalysisRequest):
    """
    Analyze a carbon project using AI to assess its credibility and impact.
    """
    try:
        result = llm_service.analyze_carbon_project(request.project_data)
        
        if not result.get("success", False):
            raise HTTPException(status_code=400, detail=result.get("error", "Failed to analyze carbon project"))
        
        return result
        
    except Exception as e:
        logger.error(f"Error analyzing carbon project: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/verify-satellite-imagery")
async def verify_satellite_imagery(request: SatelliteImageryRequest):
    """
    Use LLM to help interpret satellite imagery analysis results.
    """
    try:
        result = llm_service.verify_satellite_imagery(
            image_description=request.image_description,
            location_data=request.location_data,
            historical_data=request.historical_data
        )
        
        if not result.get("success", False):
            raise HTTPException(status_code=400, detail=result.get("error", "Failed to verify satellite imagery"))
        
        return result
        
    except Exception as e:
        logger.error(f"Error verifying satellite imagery: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/generate-credit-description")
async def generate_credit_description(request: CreditDescriptionRequest):
    """
    Generate a natural language description of a carbon credit for marketplace listings.
    """
    try:
        result = llm_service.generate_carbon_credit_description(request.credit_data)
        
        if not result.get("success", False):
            raise HTTPException(status_code=400, detail=result.get("error", "Failed to generate credit description"))
        
        return result
        
    except Exception as e:
        logger.error(f"Error generating credit description: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/status")
async def get_llm_status():
    """
    Get the current status of the LLM service configuration.
    """
    try:
        return {
            "success": True,
            "groq_api_configured": llm_service.groq_api_key is not None,
            "default_model": llm_service.default_model,
            "api_url": llm_service.groq_api_url
        }
        
    except Exception as e:
        logger.error(f"Error getting LLM status: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))
