import uvicorn
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

if __name__ == "__main__":
    # Get configuration from environment variables
    host = os.getenv("API_HOST", "0.0.0.0")
    port = int(os.getenv("API_PORT", "8000"))
    debug = os.getenv("DEBUG", "False").lower() == "true"
    
    # Run the FastAPI application with uvicorn
    uvicorn.run(
        "terraledger.api.app:app",
        host=host,
        port=port,
        reload=debug,
        log_level="info" if not debug else "debug",
    )
    
    print(f"TerraLedger API running at http://{host}:{port}")
