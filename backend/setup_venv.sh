#!/bin/bash
# Setup script for TerraLedger backend

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install -e .

# Create example .env file if it doesn't exist
if [ ! -f .env ]; then
    echo "Creating example .env file..."
    cp .env .env.example
fi

echo "Setup complete! You can now run the API with:"
echo "python api_demo.py"
