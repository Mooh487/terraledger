"""
Tests for the AI Validator module.
"""
import pytest
import numpy as np
from unittest.mock import patch, MagicMock
from terraledger.core.ai_validator import AIValidator

class TestAIValidator:
    """Test suite for the AIValidator class."""
    
    def test_init(self):
        """Test initialization of AIValidator."""
        validator = AIValidator()
        assert validator.model is None
        assert validator.model_path is None
    
    @patch('terraledger.core.ai_validator.AIValidator.load_model')
    def test_verify_forest_without_model(self, mock_load_model):
        """Test verify_forest method when model is not available."""
        # Setup
        validator = AIValidator()
        validator.model = None
        mock_load_model.return_value = None
        
        # Mock get_satellite_imagery to return a dummy image
        validator.get_satellite_imagery = MagicMock(return_value=np.zeros((512, 512, 3)))
        
        # Execute
        result = validator.verify_forest(34.05, -118.25)
        
        # Assert
        assert result["verified"] is False
        assert result["forest_coverage"] == 0.0
        assert result["confidence"] == 0.0
        assert result["location"]["lat"] == 34.05
        assert result["location"]["lon"] == -118.25
        assert "error" in result
    
    def test_calculate_carbon_sequestration(self):
        """Test carbon sequestration calculation."""
        validator = AIValidator()
        
        # Test with different values
        assert validator.calculate_carbon_sequestration(100, 1.0) == 250.0  # Full coverage
        assert validator.calculate_carbon_sequestration(100, 0.5) == 125.0  # Half coverage
        assert validator.calculate_carbon_sequestration(100, 0.0) == 0.0    # No coverage
        assert validator.calculate_carbon_sequestration(0, 1.0) == 0.0      # No area
