"""
Hedera Consensus Service (HCS) module for TerraLedger Carbon Exchange.
This module implements the HCS-10 OpenConvAI Standard for AI agent communication.
"""
import os
import json
import time
from typing import Dict, Any, Optional, List
import logging
from dotenv import load_dotenv
from ..utils.config import Config

# Configure logging
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

class HCSService:
    """
    Service class for interacting with the Hedera Consensus Service (HCS).
    Implements the HCS-10 OpenConvAI Standard for AI agent communication.
    """
    
    def __init__(self):
        """
        Initialize the HCS service with credentials from environment variables.
        """
        self.network = os.getenv("HEDERA_NETWORK", "testnet")
        self.operator_id = os.getenv("HEDERA_OPERATOR_ID")
        self.operator_key = os.getenv("HEDERA_OPERATOR_KEY")
        self.client = None
        self.registry_topic_id = os.getenv("HCS_REGISTRY_TOPIC_ID")
        self.inbound_topic_id = None
        self.outbound_topic_id = None
        self._initialize_client()
        
    def _initialize_client(self):
        """
        Initialize the Hedera client with the provided credentials.
        """
        try:
            from hedera import Client, AccountId, PrivateKey
            
            if self.network == "testnet":
                self.client = Client.forTestnet()
            elif self.network == "mainnet":
                self.client = Client.forMainnet()
            else:
                logger.error(f"Invalid network: {self.network}")
                return
            
            # Set the operator account ID and private key
            if self.operator_id and self.operator_key:
                operator_id = AccountId.fromString(self.operator_id)
                operator_key = PrivateKey.fromString(self.operator_key)
                self.client.setOperator(operator_id, operator_key)
                logger.info(f"Hedera client initialized for {self.network}")
            else:
                logger.error("Operator ID or key not provided")
                
        except ImportError:
            logger.error("hedera-sdk-py not installed. Please install it to use this feature.")
        except Exception as e:
            logger.error(f"Error initializing Hedera client: {str(e)}")
    
    def create_topic(self, memo: str, admin_key=None, submit_key=None) -> Dict[str, Any]:
        """
        Create a new HCS topic.
        
        Args:
            memo: Topic memo string (following HCS-10 format)
            admin_key: Optional admin key for the topic
            submit_key: Optional submit key for the topic
            
        Returns:
            Dict containing topic information
        """
        try:
            from hedera import (
                TopicCreateTransaction,
                TopicId,
                Status,
                Hbar
            )
            
            if not self.client:
                return {"success": False, "error": "Hedera client not initialized"}
            
            # Create the transaction
            transaction = TopicCreateTransaction().setTopicMemo(memo)
            
            # Set keys if provided
            if admin_key:
                transaction.setAdminKey(admin_key)
            
            if submit_key:
                transaction.setSubmitKey(submit_key)
            
            # Execute the transaction
            transaction_response = transaction.execute(self.client)
            
            # Get the receipt
            receipt = transaction_response.getReceipt(self.client)
            
            # Get the topic ID
            topic_id = receipt.topicId
            
            logger.info(f"Topic created: {topic_id}")
            
            return {
                "success": True,
                "topic_id": str(topic_id),
                "memo": memo
            }
            
        except Exception as e:
            logger.error(f"Error creating topic: {str(e)}")
            return {"success": False, "error": str(e)}
    
    def submit_message(self, topic_id: str, message: Dict[str, Any], transaction_memo: str = "") -> Dict[str, Any]:
        """
        Submit a message to an HCS topic.
        
        Args:
            topic_id: Topic ID to submit to
            message: Message content as a dictionary
            transaction_memo: Optional transaction memo
            
        Returns:
            Dict containing submission results
        """
        try:
            from hedera import (
                TopicMessageSubmitTransaction,
                TopicId,
                Status,
                Hbar
            )
            
            if not self.client:
                return {"success": False, "error": "Hedera client not initialized"}
            
            # Convert message to JSON bytes
            message_bytes = json.dumps(message).encode()
            
            # Create the transaction
            transaction = (TopicMessageSubmitTransaction()
                .setTopicId(TopicId.fromString(topic_id))
                .setMessage(message_bytes)
                .setTransactionMemo(transaction_memo))
            
            # Execute the transaction
            transaction_response = transaction.execute(self.client)
            
            # Get the receipt
            receipt = transaction_response.getReceipt(self.client)
            
            # Check the status
            if receipt.status == Status.SUCCESS:
                logger.info(f"Message submitted to topic {topic_id}")
                return {
                    "success": True,
                    "topic_id": topic_id,
                    "sequence_number": receipt.topicSequenceNumber,
                    "transaction_id": str(transaction_response.transactionId)
                }
            else:
                logger.error(f"Failed to submit message: {receipt.status}")
                return {"success": False, "error": f"Failed to submit message: {receipt.status}"}
            
        except Exception as e:
            logger.error(f"Error submitting message: {str(e)}")
            return {"success": False, "error": str(e)}
    
    def initialize_agent_topics(self) -> Dict[str, Any]:
        """
        Initialize the agent's inbound and outbound topics following HCS-10 standard.
        
        Returns:
            Dict containing topic information
        """
        if not self.client:
            return {"success": False, "error": "Hedera client not initialized"}
        
        try:
            from hedera import PrivateKey
            
            # Generate keys for the topics
            admin_key = PrivateKey.generate()
            submit_key = PrivateKey.generate()
            
            # Create inbound topic with HCS-10 format memo
            ttl = "60"  # Time to live in seconds
            inbound_memo = f"hcs-10:0:{ttl}:0:{self.operator_id}"
            inbound_result = self.create_topic(inbound_memo, admin_key, None)  # Public topic
            
            if not inbound_result.get("success", False):
                return inbound_result
            
            self.inbound_topic_id = inbound_result["topic_id"]
            
            # Create outbound topic with HCS-10 format memo
            outbound_memo = f"hcs-10:0:{ttl}:1"
            outbound_result = self.create_topic(outbound_memo, admin_key, submit_key)  # Only agent can submit
            
            if not outbound_result.get("success", False):
                return outbound_result
            
            self.outbound_topic_id = outbound_result["topic_id"]
            
            # Register in the registry if a registry topic is provided
            if self.registry_topic_id:
                register_message = {
                    "p": "hcs-10",
                    "op": "register",
                    "account_id": self.operator_id,
                    "m": "Registering TerraLedger Carbon Exchange AI agent."
                }
                
                register_result = self.submit_message(
                    self.registry_topic_id,
                    register_message,
                    "hcs-10:op:0:0"
                )
                
                if not register_result.get("success", False):
                    logger.warning(f"Failed to register in registry: {register_result.get('error')}")
            
            return {
                "success": True,
                "inbound_topic_id": self.inbound_topic_id,
                "outbound_topic_id": self.outbound_topic_id
            }
            
        except Exception as e:
            logger.error(f"Error initializing agent topics: {str(e)}")
            return {"success": False, "error": str(e)}
    
    def create_connection_topic(self, connected_account_id: str, connection_id: str) -> Dict[str, Any]:
        """
        Create a connection topic between two agents.
        
        Args:
            connected_account_id: Account ID of the connected agent
            connection_id: Unique connection identifier
            
        Returns:
            Dict containing topic information
        """
        if not self.client or not self.inbound_topic_id:
            return {"success": False, "error": "HCS service not properly initialized"}
        
        try:
            from hedera import PrivateKey, KeyList
            
            # Generate a threshold key for the connection topic
            admin_key = PrivateKey.generate()
            
            # Create a threshold key that requires both agents to sign
            # In a real implementation, we would use the public keys of both agents
            threshold_key = KeyList.withThreshold(2)
            
            # Create connection topic with HCS-10 format memo
            ttl = "60"  # Time to live in seconds
            connection_memo = f"hcs-10:1:{ttl}:2:{self.inbound_topic_id}:{connection_id}"
            connection_result = self.create_topic(connection_memo, admin_key, threshold_key)
            
            if not connection_result.get("success", False):
                return connection_result
            
            connection_topic_id = connection_result["topic_id"]
            
            # Notify the connected agent about the connection
            if self.inbound_topic_id:
                connection_created_message = {
                    "p": "hcs-10",
                    "op": "connection_created",
                    "connection_topic_id": connection_topic_id,
                    "connected_account_id": connected_account_id,
                    "operator_id": f"{self.operator_id}@{connected_account_id}",
                    "connection_id": connection_id,
                    "m": "Connection established."
                }
                
                self.submit_message(
                    self.inbound_topic_id,
                    connection_created_message,
                    "hcs-10:op:4:1"
                )
            
            return {
                "success": True,
                "connection_topic_id": connection_topic_id,
                "connected_account_id": connected_account_id,
                "connection_id": connection_id
            }
            
        except Exception as e:
            logger.error(f"Error creating connection topic: {str(e)}")
            return {"success": False, "error": str(e)}
    
    def send_message(self, connection_topic_id: str, connected_account_id: str, message_content: str) -> Dict[str, Any]:
        """
        Send a message to a connection topic.
        
        Args:
            connection_topic_id: Topic ID of the connection
            connected_account_id: Account ID of the connected agent
            message_content: Message content
            
        Returns:
            Dict containing submission results
        """
        if not self.client:
            return {"success": False, "error": "Hedera client not initialized"}
        
        try:
            message = {
                "p": "hcs-10",
                "op": "message",
                "operator_id": f"{self.operator_id}@{connected_account_id}",
                "data": message_content,
                "m": "Standard communication."
            }
            
            return self.submit_message(
                connection_topic_id,
                message,
                "hcs-10:op:6:3"
            )
            
        except Exception as e:
            logger.error(f"Error sending message: {str(e)}")
            return {"success": False, "error": str(e)}
    
    def request_transaction_approval(self, connection_topic_id: str, connected_account_id: str, 
                                    schedule_id: str, transaction_data: str) -> Dict[str, Any]:
        """
        Request approval for a transaction.
        
        Args:
            connection_topic_id: Topic ID of the connection
            connected_account_id: Account ID of the connected agent
            schedule_id: Schedule ID of the transaction
            transaction_data: Description of the transaction
            
        Returns:
            Dict containing submission results
        """
        if not self.client:
            return {"success": False, "error": "Hedera client not initialized"}
        
        try:
            message = {
                "p": "hcs-10",
                "op": "transaction",
                "operator_id": f"{self.operator_id}@{connected_account_id}",
                "schedule_id": schedule_id,
                "data": transaction_data,
                "m": "For your approval."
            }
            
            return self.submit_message(
                connection_topic_id,
                message,
                "hcs-10:op:7:3"
            )
            
        except Exception as e:
            logger.error(f"Error requesting transaction approval: {str(e)}")
            return {"success": False, "error": str(e)}
