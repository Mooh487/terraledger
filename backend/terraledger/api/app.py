from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Create FastAPI app
app = FastAPI(
    title="TerraLedger Carbon Exchange API",
    description="A hyper-transparent, AI-verified carbon credit marketplace using Hedera's immutable ledger",
    version="0.1.0",
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Root endpoint
@app.get("/")
async def root():
    return {
        "message": "Welcome to TerraLedger Carbon Exchange API",
        "status": "online",
        "version": "0.1.0",
    }

# Health check endpoint
@app.get("/health")
async def health_check():
    return {"status": "healthy"}

# Import and include routers
from terraledger.api.routers import carbon_credits, hcs, llm

# Include routers with proper prefixes and tags
app.include_router(carbon_credits.router, prefix="/api/v1/carbon-credits", tags=["Carbon Credits"])
app.include_router(hcs.router, prefix="/api/v1/hcs", tags=["Hedera Consensus Service"])
app.include_router(llm.router, prefix="/api/v1/llm", tags=["AI & LLM Services"])
