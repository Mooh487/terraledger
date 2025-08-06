"""
Hedera Service module for TerraLedger Carbon Exchange.
This module handles interactions with the Hedera network.
"""
import os
from typing import Dict, Any, Optional, Tuple
import logging
from dotenv import load_dotenv

# Configure logging
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

class HederaService:
    """
    Service class for interacting with the Hedera network.
    Handles token creation, minting, and transactions.
    """
    
    def __init__(self):
        """
        Initialize the Hedera service with credentials from environment variables.
        """
        self.network = os.getenv("HEDERA_NETWORK", "testnet")
        self.operator_id = os.getenv("HEDERA_OPERATOR_ID")
        self.operator_key = os.getenv("HEDERA_OPERATOR_KEY")
        self.client = None
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
    
    def create_nft_token(self, name: str, symbol: str, memo: str = "") -> Dict[str, Any]:
        """
        Create a new NFT token on the Hedera network.
        
        Args:
            name: Token name
            symbol: Token symbol
            memo: Optional memo for the token
            
        Returns:
            Dict containing token information
        """
        try:
            from hedera import (
                TokenCreateTransaction,
                TokenType,
                TokenSupplyType,
                TokenMintTransaction,
                Hbar,
                Status
            )
            
            if not self.client:
                return {"success": False, "error": "Hedera client not initialized"}
            
            # Create the NFT token
            transaction = (TokenCreateTransaction()
                .setTokenName(name)
                .setTokenSymbol(symbol)
                .setTokenType(TokenType.NON_FUNGIBLE_UNIQUE)
                .setSupplyType(TokenSupplyType.FINITE)
                .setMaxSupply(1000000)
                .setTreasuryAccountId(self.client.getOperatorAccountId())
                .setAdminKey(self.client.getOperatorPublicKey())
                .setSupplyKey(self.client.getOperatorPublicKey())
                .setFreezeKey(self.client.getOperatorPublicKey())
                .setWipeKey(self.client.getOperatorPublicKey())
                .setInitialSupply(0)
                .setTransactionMemo(memo)
                .freezeWith(self.client))
            
            # Sign and submit the transaction
            transaction_response = transaction.sign(
                self.client.getOperatorPublicKey()
            ).execute(self.client)
            
            # Get the receipt
            receipt = transaction_response.getReceipt(self.client)
            
            # Get the token ID
            token_id = receipt.tokenId
            
            logger.info(f"NFT token created: {token_id}")
            
            return {
                "success": True,
                "token_id": str(token_id),
                "name": name,
                "symbol": symbol,
                "memo": memo
            }
            
        except Exception as e:
            logger.error(f"Error creating NFT token: {str(e)}")
            return {"success": False, "error": str(e)}
    
    def mint_carbon_nft(self, token_id: str, metadata: Dict[str, Any]) -> Dict[str, Any]:
        """
        Mint a carbon credit NFT with metadata.
        
        Args:
            token_id: Token ID to mint
            metadata: Metadata for the NFT
            
        Returns:
            Dict containing minting results
        """
        try:
            from hedera import (
                TokenMintTransaction,
                TokenId,
                Status,
                Hbar
            )
            import json
            
            if not self.client:
                return {"success": False, "error": "Hedera client not initialized"}
            
            # Convert metadata to bytes
            metadata_bytes = json.dumps(metadata).encode()
            
            # Create the mint transaction
            transaction = (TokenMintTransaction()
                .setTokenId(TokenId.fromString(token_id))
                .addMetadata(metadata_bytes)
                .freezeWith(self.client))
            
            # Sign and submit the transaction
            transaction_response = transaction.sign(
                self.client.getOperatorPublicKey()
            ).execute(self.client)
            
            # Get the receipt
            receipt = transaction_response.getReceipt(self.client)
            
            # Check the status
            if receipt.status == Status.SUCCESS:
                logger.info(f"NFT minted successfully for token {token_id}")
                return {
                    "success": True,
                    "token_id": token_id,
                    "serial_number": receipt.serials[0].low,
                    "metadata": metadata
                }
            else:
                logger.error(f"Failed to mint NFT: {receipt.status}")
                return {"success": False, "error": f"Failed to mint NFT: {receipt.status}"}
            
        except Exception as e:
            logger.error(f"Error minting carbon NFT: {str(e)}")
            return {"success": False, "error": str(e)}
    
    def update_nft_metadata(self, token_id: str, serial_number: int, metadata: Dict[str, Any]) -> Dict[str, Any]:
        """
        Update the metadata of an existing NFT.
        
        Args:
            token_id: Token ID
            serial_number: Serial number of the NFT
            metadata: New metadata
            
        Returns:
            Dict containing update results
        """
        # Note: Hedera doesn't directly support updating NFT metadata
        # This would typically be implemented using a custom smart contract or HCS
        # For now, we'll just log this as a placeholder
        logger.info(f"Update NFT metadata requested for token {token_id}, serial {serial_number}")
        return {
            "success": False,
            "error": "Direct NFT metadata updates not supported by Hedera. Use HCS or a smart contract."
        }
