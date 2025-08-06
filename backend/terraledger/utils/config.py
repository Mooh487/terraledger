"""
Configuration utilities for TerraLedger Carbon Exchange.
"""
import os
from typing import Dict, Any, Optional
from dotenv import load_dotenv
import logging

# Configure logging
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

class Config:
    """
    Configuration class for TerraLedger Carbon Exchange.
    Handles environment variables and configuration settings.
    """
    
    @staticmethod
    def get_hedera_config() -> Dict[str, str]:
        """
        Get Hedera network configuration from environment variables.
        
        Returns:
            Dict containing Hedera configuration
        """
        return {
            "network": os.getenv("HEDERA_NETWORK", "testnet"),
            "operator_id": os.getenv("HEDERA_OPERATOR_ID", ""),
            "operator_key": os.getenv("HEDERA_OPERATOR_KEY", "")
        }
    
    @staticmethod
    def get_api_config() -> Dict[str, Any]:
        """
        Get API configuration from environment variables.
        
        Returns:
            Dict containing API configuration
        """
        return {
            "host": os.getenv("API_HOST", "0.0.0.0"),
            "port": int(os.getenv("API_PORT", "8000")),
            "debug": os.getenv("DEBUG", "False").lower() == "true"
        }
    
    @staticmethod
    def get_sentinel_hub_config() -> Dict[str, str]:
        """
        Get Sentinel Hub configuration from environment variables.
        
        Returns:
            Dict containing Sentinel Hub configuration
        """
        return {
            "instance_id": os.getenv("SENTINEL_HUB_INSTANCE_ID", ""),
            "api_key": os.getenv("SENTINEL_HUB_API_KEY", "")
        }
    
    @staticmethod
    def get_database_url() -> str:
        """
        Get database URL from environment variables.
        
        Returns:
            Database URL string
        """
        return os.getenv("DATABASE_URL", "sqlite:///./terraledger.db")
    
    @staticmethod
    def get_secret_key() -> str:
        """
        Get secret key for security from environment variables.
        
        Returns:
            Secret key string
        """
        return os.getenv("SECRET_KEY", "default-insecure-key")
    
    @staticmethod
    def get_log_level() -> str:
        """
        Get logging level from environment variables.
        
        Returns:
            Logging level string
        """
        return os.getenv("LOG_LEVEL", "INFO")
    
    @staticmethod
    def configure_logging():
        """
        Configure logging based on environment variables.
        """
        log_level = Config.get_log_level()
        numeric_level = getattr(logging, log_level.upper(), None)
        if not isinstance(numeric_level, int):
            numeric_level = logging.INFO
        
        logging.basicConfig(
            level=numeric_level,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        logger.info(f"Logging configured with level {log_level}")
