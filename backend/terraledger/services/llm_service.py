"""
LLM Service module for TerraLedger Carbon Exchange.
This module handles interactions with LLM APIs, specifically Groq.
"""
import os
import json
import requests
from typing import Dict, Any, List, Optional
import logging
from dotenv import load_dotenv

# Configure logging
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

class LLMService:
    """
    Service class for interacting with LLM APIs.
    Currently supports Groq API.
    """
    
    def __init__(self):
        """
        Initialize the LLM service with API keys from environment variables.
        """
        self.groq_api_key = os.getenv("GROQ_API_KEY")
        self.groq_api_url = "https://api.groq.com/openai/v1/chat/completions"
        self.default_model = os.getenv("GROQ_MODEL", "llama3-70b-8192")
        
        if not self.groq_api_key:
            logger.warning("GROQ_API_KEY not found in environment variables")
    
    def generate_response(self, 
                         prompt: str, 
                         system_message: Optional[str] = None,
                         conversation_history: Optional[List[Dict[str, str]]] = None,
                         model: Optional[str] = None,
                         temperature: float = 0.7,
                         max_tokens: int = 1024) -> Dict[str, Any]:
        """
        Generate a response from the LLM using Groq API.
        
        Args:
            prompt: User prompt
            system_message: Optional system message to guide the model
            conversation_history: Optional conversation history
            model: Optional model name (defaults to llama3-70b-8192)
            temperature: Sampling temperature (0.0 to 1.0)
            max_tokens: Maximum tokens to generate
            
        Returns:
            Dict containing the response
        """
        if not self.groq_api_key:
            return {"success": False, "error": "Groq API key not configured"}
        
        try:
            # Prepare the messages
            messages = []
            
            # Add system message if provided
            if system_message:
                messages.append({"role": "system", "content": system_message})
            
            # Add conversation history if provided
            if conversation_history:
                messages.extend(conversation_history)
            
            # Add the current prompt
            messages.append({"role": "user", "content": prompt})
            
            # Prepare the request payload
            payload = {
                "model": model or self.default_model,
                "messages": messages,
                "temperature": temperature,
                "max_tokens": max_tokens
            }
            
            # Set up headers
            headers = {
                "Authorization": f"Bearer {self.groq_api_key}",
                "Content-Type": "application/json"
            }
            
            # Make the API request
            response = requests.post(
                self.groq_api_url,
                headers=headers,
                json=payload
            )
            
            # Check if the request was successful
            if response.status_code == 200:
                result = response.json()
                return {
                    "success": True,
                    "content": result["choices"][0]["message"]["content"],
                    "model": result.get("model", model or self.default_model),
                    "usage": result.get("usage", {})
                }
            else:
                logger.error(f"Error from Groq API: {response.status_code} - {response.text}")
                return {
                    "success": False,
                    "error": f"API Error: {response.status_code}",
                    "details": response.text
                }
                
        except Exception as e:
            logger.error(f"Error generating LLM response: {str(e)}")
            return {"success": False, "error": str(e)}
    
    def analyze_carbon_project(self, project_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Analyze a carbon project using the LLM to assess its credibility and impact.
        
        Args:
            project_data: Dictionary containing project details
            
        Returns:
            Dict containing analysis results
        """
        system_message = """
        You are an expert in carbon credit verification and environmental impact assessment.
        Analyze the provided carbon project data and provide an assessment of:
        1. Project credibility (high/medium/low) with justification
        2. Environmental impact potential (high/medium/low) with justification
        3. Risks and concerns
        4. Recommendations for improvement
        
        Base your assessment on scientific principles and best practices in carbon markets.
        """
        
        # Format the project data as a string
        project_description = json.dumps(project_data, indent=2)
        
        prompt = f"""
        Please analyze the following carbon project:
        
        {project_description}
        
        Provide a comprehensive assessment following the guidelines in the system message.
        """
        
        return self.generate_response(
            prompt=prompt,
            system_message=system_message,
            temperature=0.3,  # Lower temperature for more factual responses
            max_tokens=2048   # Allow for detailed analysis
        )
    
    def verify_satellite_imagery(self, 
                               image_description: str, 
                               location_data: Dict[str, Any],
                               historical_data: Optional[List[Dict[str, Any]]] = None) -> Dict[str, Any]:
        """
        Use LLM to help interpret satellite imagery analysis results.
        
        Args:
            image_description: Description of the satellite imagery
            location_data: Data about the location
            historical_data: Optional historical data for comparison
            
        Returns:
            Dict containing verification results
        """
        system_message = """
        You are an expert in satellite imagery analysis for environmental monitoring.
        Analyze the provided satellite imagery description and location data to assess:
        1. Evidence of forest cover or deforestation
        2. Changes over time (if historical data is provided)
        3. Confidence level in the assessment
        4. Recommendations for further verification
        
        Provide a scientific assessment based on the available data.
        """
        
        # Format the data
        location_str = json.dumps(location_data, indent=2)
        historical_str = ""
        if historical_data:
            historical_str = f"\nHistorical data:\n{json.dumps(historical_data, indent=2)}"
        
        prompt = f"""
        Please analyze the following satellite imagery and location data:
        
        Image description:
        {image_description}
        
        Location data:
        {location_str}
        {historical_str}
        
        Provide a comprehensive assessment following the guidelines in the system message.
        """
        
        return self.generate_response(
            prompt=prompt,
            system_message=system_message,
            temperature=0.4,
            max_tokens=1536
        )
    
    def generate_carbon_credit_description(self, credit_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Generate a natural language description of a carbon credit for marketplace listings.
        
        Args:
            credit_data: Data about the carbon credit
            
        Returns:
            Dict containing the generated description
        """
        system_message = """
        You are a carbon market expert creating compelling and accurate descriptions for carbon credit listings.
        Generate a clear, informative, and engaging description that includes:
        1. Project location and type
        2. Environmental benefits
        3. Verification standards met
        4. Impact metrics
        5. Unique selling points
        
        The description should be factual, transparent, and avoid greenwashing.
        """
        
        # Format the credit data
        credit_str = json.dumps(credit_data, indent=2)
        
        prompt = f"""
        Please generate a marketplace description for the following carbon credit:
        
        {credit_str}
        
        Create a compelling but factual description following the guidelines in the system message.
        """
        
        return self.generate_response(
            prompt=prompt,
            system_message=system_message,
            temperature=0.7,  # Higher temperature for more creative writing
            max_tokens=1024
        )
