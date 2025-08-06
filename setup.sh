#!/bin/bash

# TerraLedger Carbon Exchange - Project Setup Script
# This script sets up the complete development environment

set -e  # Exit on any error

echo "🌍 Welcome to TerraLedger Carbon Exchange Setup!"
echo "=================================================="

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

print_header() {
    echo -e "${BLUE}$1${NC}"
}

# Check prerequisites
check_prerequisites() {
    print_header "🔍 Checking Prerequisites..."
    
    # Check Node.js
    if ! command -v node &> /dev/null; then
        print_error "Node.js is not installed. Please install Node.js 18+ from https://nodejs.org/"
        exit 1
    fi
    
    NODE_VERSION=$(node --version | cut -d'v' -f2 | cut -d'.' -f1)
    if [ "$NODE_VERSION" -lt 18 ]; then
        print_error "Node.js version 18+ is required. Current version: $(node --version)"
        exit 1
    fi
    print_status "Node.js $(node --version) ✓"
    
    # Check Python
    if ! command -v python3 &> /dev/null; then
        print_error "Python 3 is not installed. Please install Python 3.9+ from https://python.org/"
        exit 1
    fi
    
    PYTHON_VERSION=$(python3 --version | cut -d' ' -f2 | cut -d'.' -f1-2)
    print_status "Python $(python3 --version) ✓"
    
    # Check pip
    if ! command -v pip3 &> /dev/null; then
        print_error "pip3 is not installed. Please install pip3"
        exit 1
    fi
    print_status "pip3 ✓"
    
    # Check git
    if ! command -v git &> /dev/null; then
        print_error "Git is not installed. Please install Git from https://git-scm.com/"
        exit 1
    fi
    print_status "Git $(git --version) ✓"
    
    echo ""
}

# Setup backend
setup_backend() {
    print_header "🐍 Setting up Backend (TerraLedger API)..."
    
    cd backend
    
    # Create virtual environment
    print_status "Creating Python virtual environment..."
    python3 -m venv venv
    
    # Activate virtual environment
    print_status "Activating virtual environment..."
    source venv/bin/activate
    
    # Upgrade pip
    print_status "Upgrading pip..."
    pip install --upgrade pip
    
    # Install dependencies
    print_status "Installing Python dependencies..."
    pip install -e .
    
    # Create .env file if it doesn't exist
    if [ ! -f .env ]; then
        print_status "Creating .env file from template..."
        cp .env .env.example
        print_warning "Please edit backend/.env with your actual credentials!"
        print_warning "Required: HEDERA_OPERATOR_ID, HEDERA_OPERATOR_KEY, GROQ_API_KEY"
    fi
    
    # Run tests
    print_status "Running backend tests..."
    pytest --tb=short
    
    cd ..
    print_status "Backend setup complete! ✓"
    echo ""
}

# Setup frontend
setup_frontend() {
    print_header "⚛️ Setting up Frontend (TerraGold)..."
    
    cd frontend
    
    # Install dependencies
    print_status "Installing Node.js dependencies..."
    npm install
    
    # Run linting
    print_status "Running ESLint..."
    npm run lint
    
    # Build the project to verify everything works
    print_status "Building frontend to verify setup..."
    npm run build
    
    cd ..
    print_status "Frontend setup complete! ✓"
    echo ""
}

# Setup project root
setup_project_root() {
    print_header "📦 Setting up Project Root..."
    
    # Install concurrently for running both servers
    print_status "Installing project dependencies..."
    npm install
    
    print_status "Project root setup complete! ✓"
    echo ""
}

# Create development scripts
create_dev_scripts() {
    print_header "🛠️ Creating Development Scripts..."
    
    # Create start script
    cat > start-dev.sh << 'EOF'
#!/bin/bash
echo "🚀 Starting TerraLedger Development Environment..."
echo "Frontend: http://localhost:5173"
echo "Backend API: http://localhost:8000"
echo "API Docs: http://localhost:8000/docs"
echo ""
echo "Press Ctrl+C to stop all services"
npm run dev
EOF
    chmod +x start-dev.sh
    
    # Create backend-only script
    cat > start-backend.sh << 'EOF'
#!/bin/bash
echo "🐍 Starting TerraLedger Backend..."
cd backend
source venv/bin/activate
python api_demo.py
EOF
    chmod +x start-backend.sh
    
    # Create frontend-only script
    cat > start-frontend.sh << 'EOF'
#!/bin/bash
echo "⚛️ Starting TerraGold Frontend..."
cd frontend
npm run dev
EOF
    chmod +x start-frontend.sh
    
    print_status "Development scripts created! ✓"
    echo ""
}

# Display final instructions
show_final_instructions() {
    print_header "🎉 Setup Complete!"
    echo ""
    echo "Your TerraLedger Carbon Exchange development environment is ready!"
    echo ""
    echo "📋 Next Steps:"
    echo "1. Edit backend/.env with your credentials:"
    echo "   - HEDERA_OPERATOR_ID (your Hedera testnet account)"
    echo "   - HEDERA_OPERATOR_KEY (your private key)"
    echo "   - GROQ_API_KEY (your Groq API key)"
    echo ""
    echo "2. Start the development environment:"
    echo "   ./start-dev.sh    # Start both frontend and backend"
    echo "   ./start-backend.sh # Start only backend"
    echo "   ./start-frontend.sh # Start only frontend"
    echo ""
    echo "3. Access the applications:"
    echo "   🌐 Frontend (TerraGold): http://localhost:5173"
    echo "   🔧 Backend API: http://localhost:8000"
    echo "   📖 API Documentation: http://localhost:8000/docs"
    echo ""
    echo "📚 Documentation:"
    echo "   - Project README: ./README.md"
    echo "   - Backend README: ./backend/README.md"
    echo "   - Frontend README: ./frontend/README.md"
    echo "   - Contributing Guide: ./CONTRIBUTING.md"
    echo ""
    echo "🆘 Need Help?"
    echo "   - Discord: https://discord.gg/terraledger"
    echo "   - Email: support@terraledger.com"
    echo "   - Issues: https://github.com/terraledger/issues"
    echo ""
    echo "🌍 Happy coding! Let's build the future of carbon markets together! 🌱"
}

# Main execution
main() {
    check_prerequisites
    setup_project_root
    setup_backend
    setup_frontend
    create_dev_scripts
    show_final_instructions
}

# Run main function
main
