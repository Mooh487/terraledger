"""
HCS (Hedera Consensus Service) API router for TerraLedger Carbon Exchange.
Implements HCS-10 OpenConvAI Standard for AI agent communication.
"""
from fastapi import APIRouter, HTTPException, Body
from typing import Dict, Any, Optional, List
from pydantic import BaseModel
from ...services.hcs_service import HCSService
import logging

# Configure logging
logger = logging.getLogger(__name__)

# Create router
router = APIRouter()

# Initialize HCS service
hcs_service = HCSService()

# Pydantic models for request/response
class TopicCreateRequest(BaseModel):
    memo: str
    admin_key: Optional[str] = None
    submit_key: Optional[str] = None

class MessageSubmitRequest(BaseModel):
    topic_id: str
    message: Dict[str, Any]
    transaction_memo: Optional[str] = ""

class ConnectionRequest(BaseModel):
    connected_account_id: str
    connection_id: str

class MessageRequest(BaseModel):
    connection_topic_id: str
    connected_account_id: str
    message_content: str

class TransactionApprovalRequest(BaseModel):
    connection_topic_id: str
    connected_account_id: str
    schedule_id: str
    transaction_data: str

@router.post("/topics", status_code=201)
async def create_topic(request: TopicCreateRequest):
    """
    Create a new HCS topic.
    """
    try:
        result = hcs_service.create_topic(
            memo=request.memo,
            admin_key=request.admin_key,
            submit_key=request.submit_key
        )
        
        if not result.get("success", False):
            raise HTTPException(status_code=400, detail=result.get("error", "Failed to create topic"))
        
        return result
        
    except Exception as e:
        logger.error(f"Error creating topic: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/topics/{topic_id}/messages", status_code=201)
async def submit_message(topic_id: str, request: MessageSubmitRequest):
    """
    Submit a message to an HCS topic.
    """
    try:
        result = hcs_service.submit_message(
            topic_id=topic_id,
            message=request.message,
            transaction_memo=request.transaction_memo
        )
        
        if not result.get("success", False):
            raise HTTPException(status_code=400, detail=result.get("error", "Failed to submit message"))
        
        return result
        
    except Exception as e:
        logger.error(f"Error submitting message: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/agent/initialize", status_code=201)
async def initialize_agent():
    """
    Initialize the agent's inbound and outbound topics following HCS-10 standard.
    """
    try:
        result = hcs_service.initialize_agent_topics()
        
        if not result.get("success", False):
            raise HTTPException(status_code=400, detail=result.get("error", "Failed to initialize agent topics"))
        
        return result
        
    except Exception as e:
        logger.error(f"Error initializing agent: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/connections", status_code=201)
async def create_connection(request: ConnectionRequest):
    """
    Create a connection topic between two agents.
    """
    try:
        result = hcs_service.create_connection_topic(
            connected_account_id=request.connected_account_id,
            connection_id=request.connection_id
        )
        
        if not result.get("success", False):
            raise HTTPException(status_code=400, detail=result.get("error", "Failed to create connection"))
        
        return result
        
    except Exception as e:
        logger.error(f"Error creating connection: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/connections/messages", status_code=201)
async def send_message(request: MessageRequest):
    """
    Send a message to a connection topic.
    """
    try:
        result = hcs_service.send_message(
            connection_topic_id=request.connection_topic_id,
            connected_account_id=request.connected_account_id,
            message_content=request.message_content
        )
        
        if not result.get("success", False):
            raise HTTPException(status_code=400, detail=result.get("error", "Failed to send message"))
        
        return result
        
    except Exception as e:
        logger.error(f"Error sending message: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/connections/transaction-approval", status_code=201)
async def request_transaction_approval(request: TransactionApprovalRequest):
    """
    Request approval for a transaction.
    """
    try:
        result = hcs_service.request_transaction_approval(
            connection_topic_id=request.connection_topic_id,
            connected_account_id=request.connected_account_id,
            schedule_id=request.schedule_id,
            transaction_data=request.transaction_data
        )
        
        if not result.get("success", False):
            raise HTTPException(status_code=400, detail=result.get("error", "Failed to request transaction approval"))
        
        return result
        
    except Exception as e:
        logger.error(f"Error requesting transaction approval: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/agent/status")
async def get_agent_status():
    """
    Get the current status of the agent's HCS configuration.
    """
    try:
        return {
            "success": True,
            "operator_id": hcs_service.operator_id,
            "network": hcs_service.network,
            "inbound_topic_id": hcs_service.inbound_topic_id,
            "outbound_topic_id": hcs_service.outbound_topic_id,
            "registry_topic_id": hcs_service.registry_topic_id,
            "client_initialized": hcs_service.client is not None
        }
        
    except Exception as e:
        logger.error(f"Error getting agent status: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))
