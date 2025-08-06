"""
Integration tests for TerraLedger Carbon Exchange.
Tests the interaction between different services and components.
"""
import pytest
import asyncio
from unittest.mock import patch, MagicMock
from terraledger.core.ai_validator import AIValidator
from terraledger.services.hedera_service import HederaService
from terraledger.services.hcs_service import HCSService
from terraledger.services.llm_service import LLMService

class TestTerraLedgerIntegration:
    """Integration test suite for TerraLedger services."""
    
    def test_carbon_credit_workflow(self):
        """Test the complete carbon credit creation workflow."""
        # Initialize services
        ai_validator = AIValidator()
        hedera_service = HederaService()
        llm_service = LLMService()
        
        # Mock project data
        project_data = {
            "project_name": "Amazon Rainforest Conservation",
            "location": {
                "latitude": -3.4653,
                "longitude": -62.2159
            },
            "acres": 1000,
            "project_description": "Conservation project in the Amazon rainforest"
        }
        
        # Step 1: Verify forest coverage using AI
        with patch.object(ai_validator, 'verify_forest') as mock_verify:
            mock_verify.return_value = {
                "verified": True,
                "forest_coverage": 0.85,
                "confidence": 0.92,
                "location": project_data["location"],
                "timestamp": "2023-01-01T00:00:00Z"
            }
            
            verification_result = ai_validator.verify_forest(
                project_data["location"]["latitude"],
                project_data["location"]["longitude"]
            )
            
            assert verification_result["verified"] is True
            assert verification_result["forest_coverage"] == 0.85
        
        # Step 2: Calculate carbon sequestration
        carbon_sequestration = ai_validator.calculate_carbon_sequestration(
            project_data["acres"],
            verification_result["forest_coverage"]
        )
        
        assert carbon_sequestration == 2125.0  # 1000 * 0.85 * 2.5
        
        # Step 3: Analyze project with LLM (mocked)
        with patch.object(llm_service, 'analyze_carbon_project') as mock_analyze:
            mock_analyze.return_value = {
                "success": True,
                "content": "High credibility project with strong environmental impact potential.",
                "model": "llama3-70b-8192",
                "usage": {"tokens": 150}
            }
            
            analysis_result = llm_service.analyze_carbon_project(project_data)
            
            assert analysis_result["success"] is True
            assert "High credibility" in analysis_result["content"]
        
        # Step 4: Create NFT token (mocked)
        with patch.object(hedera_service, 'create_nft_token') as mock_create_token:
            mock_create_token.return_value = {
                "success": True,
                "token_id": "0.0.123456",
                "name": "TerraLedger Carbon - Amazon Rainforest Conservation",
                "symbol": "TLC"
            }
            
            token_result = hedera_service.create_nft_token(
                name=f"TerraLedger Carbon - {project_data['project_name']}",
                symbol="TLC",
                memo=f"Carbon credits for {project_data['project_name']}"
            )
            
            assert token_result["success"] is True
            assert token_result["token_id"] == "0.0.123456"
        
        # Step 5: Mint NFT with metadata (mocked)
        with patch.object(hedera_service, 'mint_carbon_nft') as mock_mint:
            mock_mint.return_value = {
                "success": True,
                "token_id": "0.0.123456",
                "serial_number": 1,
                "metadata": {
                    "acres": project_data["acres"],
                    "forest_coverage": verification_result["forest_coverage"],
                    "carbon_sequestration": carbon_sequestration
                }
            }
            
            mint_result = hedera_service.mint_carbon_nft(
                token_id=token_result["token_id"],
                metadata={
                    "acres": project_data["acres"],
                    "location": project_data["location"],
                    "project_name": project_data["project_name"],
                    "forest_coverage": verification_result["forest_coverage"],
                    "carbon_sequestration": carbon_sequestration
                }
            )
            
            assert mint_result["success"] is True
            assert mint_result["serial_number"] == 1
    
    def test_hcs_agent_communication(self):
        """Test HCS agent communication workflow."""
        hcs_service = HCSService()
        
        # Mock the Hedera client
        with patch.object(hcs_service, 'client') as mock_client:
            mock_client.getOperatorAccountId.return_value = "0.0.123456"
            
            # Test agent initialization (mocked)
            with patch.object(hcs_service, 'initialize_agent_topics') as mock_init:
                mock_init.return_value = {
                    "success": True,
                    "inbound_topic_id": "0.0.789101",
                    "outbound_topic_id": "0.0.789102"
                }
                
                init_result = hcs_service.initialize_agent_topics()
                
                assert init_result["success"] is True
                assert "inbound_topic_id" in init_result
                assert "outbound_topic_id" in init_result
            
            # Test connection creation (mocked)
            with patch.object(hcs_service, 'create_connection_topic') as mock_connection:
                mock_connection.return_value = {
                    "success": True,
                    "connection_topic_id": "0.0.567890",
                    "connected_account_id": "0.0.654321",
                    "connection_id": "12345"
                }
                
                connection_result = hcs_service.create_connection_topic(
                    connected_account_id="0.0.654321",
                    connection_id="12345"
                )
                
                assert connection_result["success"] is True
                assert connection_result["connection_topic_id"] == "0.0.567890"
            
            # Test message sending (mocked)
            with patch.object(hcs_service, 'send_message') as mock_send:
                mock_send.return_value = {
                    "success": True,
                    "topic_id": "0.0.567890",
                    "sequence_number": 1,
                    "transaction_id": "0.0.123456@1234567890.123456789"
                }
                
                message_result = hcs_service.send_message(
                    connection_topic_id="0.0.567890",
                    connected_account_id="0.0.654321",
                    message_content="Hello from TerraLedger AI agent!"
                )
                
                assert message_result["success"] is True
                assert message_result["sequence_number"] == 1
    
    def test_llm_carbon_analysis_workflow(self):
        """Test LLM-powered carbon project analysis workflow."""
        llm_service = LLMService()
        
        # Mock project data
        project_data = {
            "project_name": "Mangrove Restoration Project",
            "location": "Southeast Asia",
            "project_type": "Reforestation",
            "area": "500 hectares",
            "methodology": "VCS Standard",
            "verification_body": "Third-party verified"
        }
        
        # Mock LLM response for project analysis
        with patch.object(llm_service, 'analyze_carbon_project') as mock_analyze:
            mock_analyze.return_value = {
                "success": True,
                "content": """
                Project Credibility: HIGH
                - Third-party verification provides strong assurance
                - VCS Standard is well-recognized methodology
                - Mangrove restoration has proven carbon sequestration benefits
                
                Environmental Impact: HIGH
                - Mangroves are highly effective carbon sinks
                - Additional biodiversity and coastal protection benefits
                - 500 hectares represents significant scale
                
                Risks: LOW
                - Established methodology reduces technical risk
                - Southeast Asia has favorable climate for mangroves
                
                Recommendations:
                - Monitor long-term survival rates
                - Implement community engagement programs
                """,
                "model": "llama3-70b-8192",
                "usage": {"total_tokens": 250}
            }
            
            analysis_result = llm_service.analyze_carbon_project(project_data)
            
            assert analysis_result["success"] is True
            assert "HIGH" in analysis_result["content"]
            assert "Mangrove" in analysis_result["content"]
        
        # Mock satellite imagery verification
        with patch.object(llm_service, 'verify_satellite_imagery') as mock_verify:
            mock_verify.return_value = {
                "success": True,
                "content": """
                Satellite Imagery Analysis:
                
                Forest Cover Assessment: CONFIRMED
                - Clear evidence of mangrove vegetation in target area
                - Healthy canopy coverage visible in recent imagery
                - No signs of recent deforestation or degradation
                
                Confidence Level: HIGH (90%)
                - High-resolution imagery available
                - Clear spectral signatures of mangrove vegetation
                - Consistent with ground-truth data
                
                Recommendations:
                - Continue monthly monitoring
                - Cross-reference with tide data for mangrove health
                """,
                "model": "llama3-70b-8192",
                "usage": {"total_tokens": 180}
            }
            
            imagery_result = llm_service.verify_satellite_imagery(
                image_description="High-resolution satellite image showing mangrove forest",
                location_data={"region": "Southeast Asia", "coordinates": "1.3521° N, 103.8198° E"},
                historical_data=[{"date": "2023-01-01", "coverage": 0.85}]
            )
            
            assert imagery_result["success"] is True
            assert "CONFIRMED" in imagery_result["content"]
            assert "90%" in imagery_result["content"]
        
        # Mock credit description generation
        with patch.object(llm_service, 'generate_carbon_credit_description') as mock_description:
            mock_description.return_value = {
                "success": True,
                "content": """
                Premium Mangrove Restoration Carbon Credits - Southeast Asia
                
                Support coastal ecosystem restoration while offsetting your carbon footprint with these high-quality carbon credits from our verified mangrove restoration project in Southeast Asia.
                
                Key Features:
                • 500 hectares of mangrove restoration
                • VCS Standard verified methodology
                • Third-party audited and certified
                • Additional biodiversity and coastal protection benefits
                • Transparent monitoring via satellite imagery
                
                Environmental Impact:
                • High carbon sequestration potential (up to 10x more than terrestrial forests)
                • Critical habitat restoration for marine species
                • Natural coastal defense against storms and erosion
                • Community livelihood enhancement
                
                Each credit represents 1 metric ton of CO2 equivalent sequestered through sustainable mangrove restoration practices.
                """,
                "model": "llama3-70b-8192",
                "usage": {"total_tokens": 220}
            }
            
            description_result = llm_service.generate_carbon_credit_description({
                "project_type": "Mangrove Restoration",
                "location": "Southeast Asia",
                "area": "500 hectares",
                "verification": "VCS Standard"
            })
            
            assert description_result["success"] is True
            assert "Premium Mangrove" in description_result["content"]
            assert "VCS Standard" in description_result["content"]
