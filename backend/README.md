# TerraLedger Carbon Exchange - Backend

A hyper-transparent, AI-verified carbon credit marketplace using Hedera's immutable ledger.

## Project Structure

```
backend/
├── terraledger/
│   ├── api/               # FastAPI routes and endpoints
│   ├── core/              # Core business logic
│   ├── models/            # Pydantic models
│   ├── services/          # External service integrations
│   ├── utils/             # Utility functions
│   └── tests/             # Test suite
├── api_demo.py            # Entry point for the API
├── setup.py               # Package configuration
├── pyproject.toml         # Project metadata and tool configuration
└── .env                   # Environment variables (not committed to version control)
```

## Features

- **Dynamic Carbon NFTs**: Credits auto-update with sequestration progress via satellite/IoT data
- **Fractional Retirement**: Businesses offset micro-emissions (0.001 credits) with minimal fees
- **AI Oracle Network**: Multiple data sources for real-time verification
- **Hedera Integration**: Leveraging Hedera Token Service (HTS) and Hedera Consensus Service (HCS)
- **HCS-10 OpenConvAI Standard**: AI agent communication and discovery on Hedera Consensus Service
- **LLM-Powered Analysis**: Advanced AI analysis using Groq API for project verification and content generation
- **Real-time Monitoring**: Satellite imagery analysis with AI interpretation
- **Transparent Communication**: Decentralized agent-to-agent communication via HCS topics

## Getting Started

### Prerequisites

- Python 3.9+
- Hedera testnet account
- Sentinel Hub account (for satellite imagery)

### Installation

1. Clone the repository
2. Navigate to the backend directory
3. Create and activate a virtual environment:

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

4. Install dependencies:

```bash
pip install -e .
```

5. Configure environment variables:

Copy the `.env.example` file to `.env` and update with your credentials:

```
# Hedera Network Configuration
HEDERA_NETWORK=testnet
HEDERA_OPERATOR_ID=your-operator-id
HEDERA_OPERATOR_KEY=your-operator-key

# Sentinel Hub API
SENTINEL_HUB_INSTANCE_ID=your-instance-id
SENTINEL_HUB_API_KEY=your-api-key

# Groq API Configuration
GROQ_API_KEY=your-groq-api-key-here
GROQ_MODEL=llama3-70b-8192

# HCS Configuration
HCS_REGISTRY_TOPIC_ID=0.0.000000
```

### Running the API

```bash
python api_demo.py
```

The API will be available at http://localhost:8000

### API Documentation

Once the API is running, you can access the interactive API documentation at:

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Testing

Run the test suite with pytest:

```bash
pytest
```

## Development

### Adding a New Endpoint

1. Create a new router in `terraledger/api/routers/`
2. Add models in `terraledger/models/`
3. Implement business logic in `terraledger/core/`
4. Include the router in `terraledger/api/app.py`

## License

This project is licensed under the MIT License - see the LICENSE file for details.
