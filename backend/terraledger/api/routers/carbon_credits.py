"""
Carbon Credits API router for TerraLedger Carbon Exchange.
"""
from fastapi import APIRouter, Depends, HTTPException, Body, Query, Path
from typing import List, Dict, Any, Optional
from ...models.carbon_credit import (
    CarbonCreditCreate,
    CarbonCreditResponse,
    CarbonCreditUpdate,
    CarbonCreditVerification,
    CarbonCreditRetirement
)
from ...core.ai_validator import AIValidator
from ...services.hedera_service import HederaService
import logging

# Configure logging
logger = logging.getLogger(__name__)

# Create router
router = APIRouter()

# Initialize services
ai_validator = AIValidator()
hedera_service = HederaService()

# In-memory storage for demo purposes
# In a production environment, this would be replaced with a database
carbon_credits_db = {}

@router.post("/", response_model=CarbonCreditResponse, status_code=201)
async def create_carbon_credit(credit: CarbonCreditCreate):
    """
    Create a new carbon credit.
    """
    # Generate a unique ID for the credit
    from uuid import uuid4
    credit_id = str(uuid4())
    
    # Verify the forest using AI
    verification_result = ai_validator.verify_forest(
        credit.location.latitude, 
        credit.location.longitude
    )
    
    # Calculate carbon sequestration
    forest_coverage = verification_result.get("forest_coverage", 0.0)
    carbon_sequestration = ai_validator.calculate_carbon_sequestration(
        credit.acres, 
        forest_coverage
    )
    
    # Create the carbon credit in our "database"
    credit_data = {
        "id": credit_id,
        "acres": credit.acres,
        "location": {
            "latitude": credit.location.latitude,
            "longitude": credit.location.longitude,
            "geo_hash": credit.location.geo_hash
        },
        "project_name": credit.project_name,
        "project_description": credit.project_description,
        "owner_id": credit.owner_id,
        "token_id": None,
        "serial_number": None,
        "created_at": "2023-01-01T00:00:00Z",  # Placeholder
        "updated_at": "2023-01-01T00:00:00Z",  # Placeholder
        "verification_data": verification_result,
        "forest_coverage": forest_coverage,
        "carbon_sequestration": carbon_sequestration,
        "status": "verified" if verification_result.get("verified", False) else "rejected"
    }
    
    # Store in our "database"
    carbon_credits_db[credit_id] = credit_data
    
    # If verification was successful, mint an NFT
    if verification_result.get("verified", False):
        # Create NFT token if it doesn't exist yet
        # In a real app, we'd check if a token already exists for this project
        token_result = hedera_service.create_nft_token(
            name=f"TerraLedger Carbon - {credit.project_name}",
            symbol="TLC",
            memo=f"Carbon credits for {credit.project_name}"
        )
        
        if token_result.get("success", False):
            # Mint the NFT with the credit data as metadata
            mint_result = hedera_service.mint_carbon_nft(
                token_id=token_result["token_id"],
                metadata={
                    "credit_id": credit_id,
                    "acres": credit.acres,
                    "location": {
                        "latitude": credit.location.latitude,
                        "longitude": credit.location.longitude,
                        "geo_hash": credit.location.geo_hash
                    },
                    "project_name": credit.project_name,
                    "forest_coverage": forest_coverage,
                    "carbon_sequestration": carbon_sequestration
                }
            )
            
            if mint_result.get("success", False):
                # Update the credit with token information
                carbon_credits_db[credit_id]["token_id"] = token_result["token_id"]
                carbon_credits_db[credit_id]["serial_number"] = mint_result["serial_number"]
    
    return carbon_credits_db[credit_id]

@router.get("/", response_model=List[CarbonCreditResponse])
async def list_carbon_credits(
    owner_id: Optional[str] = Query(None, description="Filter by owner ID"),
    status: Optional[str] = Query(None, description="Filter by status")
):
    """
    List all carbon credits, with optional filtering.
    """
    credits = list(carbon_credits_db.values())
    
    # Apply filters if provided
    if owner_id:
        credits = [c for c in credits if c["owner_id"] == owner_id]
    
    if status:
        credits = [c for c in credits if c["status"] == status]
    
    return credits

@router.get("/{credit_id}", response_model=CarbonCreditResponse)
async def get_carbon_credit(credit_id: str = Path(..., description="The ID of the carbon credit")):
    """
    Get a specific carbon credit by ID.
    """
    if credit_id not in carbon_credits_db:
        raise HTTPException(status_code=404, detail="Carbon credit not found")
    
    return carbon_credits_db[credit_id]

@router.put("/{credit_id}", response_model=CarbonCreditResponse)
async def update_carbon_credit(
    credit_update: CarbonCreditUpdate,
    credit_id: str = Path(..., description="The ID of the carbon credit")
):
    """
    Update a carbon credit.
    """
    if credit_id not in carbon_credits_db:
        raise HTTPException(status_code=404, detail="Carbon credit not found")
    
    credit = carbon_credits_db[credit_id]
    
    # Update fields if provided
    update_data = credit_update.dict(exclude_unset=True)
    for key, value in update_data.items():
        if value is not None:
            credit[key] = value
    
    # Update the "updated_at" timestamp
    credit["updated_at"] = "2023-01-01T00:00:00Z"  # Placeholder
    
    # If the credit has a token_id and the status or forest_coverage has changed,
    # we would update the NFT metadata on Hedera
    if credit.get("token_id") and (
        "status" in update_data or "forest_coverage" in update_data
    ):
        # This is a placeholder - in a real app, we'd update the NFT metadata
        pass
    
    return credit

@router.post("/{credit_id}/verify", response_model=CarbonCreditResponse)
async def verify_carbon_credit(
    verification: CarbonCreditVerification,
    credit_id: str = Path(..., description="The ID of the carbon credit")
):
    """
    Verify a carbon credit using AI and satellite data.
    """
    if credit_id not in carbon_credits_db:
        raise HTTPException(status_code=404, detail="Carbon credit not found")
    
    credit = carbon_credits_db[credit_id]
    
    # Perform verification
    location = credit["location"]
    verification_result = ai_validator.verify_forest(
        location["latitude"],
        location["longitude"]
    )
    
    # Update the credit with new verification data
    credit["verification_data"] = verification_result
    credit["forest_coverage"] = verification_result.get("forest_coverage", 0.0)
    credit["carbon_sequestration"] = ai_validator.calculate_carbon_sequestration(
        credit["acres"],
        credit["forest_coverage"]
    )
    credit["status"] = "verified" if verification_result.get("verified", False) else "rejected"
    credit["updated_at"] = "2023-01-01T00:00:00Z"  # Placeholder
    
    # If the credit has a token_id, update the NFT metadata
    if credit.get("token_id"):
        # This is a placeholder - in a real app, we'd update the NFT metadata
        pass
    
    return credit

@router.post("/{credit_id}/retire", response_model=CarbonCreditResponse)
async def retire_carbon_credit(
    retirement: CarbonCreditRetirement,
    credit_id: str = Path(..., description="The ID of the carbon credit")
):
    """
    Retire a carbon credit (or a fraction of it).
    """
    if credit_id not in carbon_credits_db:
        raise HTTPException(status_code=404, detail="Carbon credit not found")
    
    credit = carbon_credits_db[credit_id]
    
    # Check if the credit is verified
    if credit["status"] != "verified":
        raise HTTPException(status_code=400, detail="Only verified credits can be retired")
    
    # In a real app, we would track partial retirements
    # For this demo, we'll just mark the entire credit as retired
    credit["status"] = "retired"
    credit["updated_at"] = "2023-01-01T00:00:00Z"  # Placeholder
    
    # If the credit has a token_id, we would update the NFT metadata
    if credit.get("token_id"):
        # This is a placeholder - in a real app, we'd update the NFT metadata
        pass
    
    return credit
