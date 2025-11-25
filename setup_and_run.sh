#!/bin/bash

# 🚀 TodoApp Backend Setup and Run Script
# This script sets up a virtual environment and runs the TodoApp backend

echo "🚀 Setting up TodoApp Backend..."

# Determine script directory for relative paths
SCRIPT_DIR="$(cd -- "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Parse arguments
AUTO_START=false
for arg in "$@"; do
    case "$arg" in
        --start|-s)
            AUTO_START=true
            ;;
    esac
done

# Navigate to the backend directory
cd "$SCRIPT_DIR"

# Check if system has python3-venv
if ! python3 -c "import venv" &> /dev/null; then
    echo "⚠️  python3-venv not available. Installing..."
    sudo apt update && sudo apt install -y python3.10-venv python3-pip
else
    echo "✅ python3-venv is already available"
fi

# Check if virtual environment already exists and is functional
if [ -d "venv" ] && [ -f "venv/bin/activate" ] && [ -f "venv/bin/python3" ]; then
    echo "✅ Virtual environment already exists"
    VENV_EXISTS=true
else
    echo "📦 Creating virtual environment..."
    # Remove any broken environments
    if [ -d "venv" ]; then
        echo "🧹 Removing incomplete virtual environment..."
        rm -rf venv
    fi
    if [ -d "todo_venv" ]; then
        echo "🧹 Removing old virtual environment..."
        rm -rf todo_venv
    fi
    
    python3 -m venv venv
    if [ $? -eq 0 ]; then
        echo "✅ Virtual environment created successfully"
        VENV_EXISTS=true
    else
        echo "❌ Failed to create virtual environment"
        exit 1
    fi
fi

# Activate virtual environment
echo "🔌 Activating virtual environment..."
source venv/bin/activate

# Check if pip needs upgrading
CURRENT_PIP_VERSION=$(pip --version 2>/dev/null | grep -o 'pip [0-9.]*' | cut -d' ' -f2 || echo "unknown")

# Simple pip upgrade check - just upgrade if version is older than 24.0
if [ "$CURRENT_PIP_VERSION" != "unknown" ]; then
    MAJOR_VERSION=$(echo "$CURRENT_PIP_VERSION" | cut -d'.' -f1)
    if [ "$MAJOR_VERSION" -lt 24 ]; then
        echo "⬆️ Upgrading pip (current: $CURRENT_PIP_VERSION)..."
        pip install --upgrade pip
    else
        echo "✅ Pip is up to date ($CURRENT_PIP_VERSION)"
    fi
else
    echo "⬆️ Upgrading pip..."
    pip install --upgrade pip
fi

# Check if dependencies are already installed
echo "🔍 Checking installed dependencies..."
PACKAGES_LIST=$(pip list 2>/dev/null)

if echo "$PACKAGES_LIST" | grep -q "fastapi" && echo "$PACKAGES_LIST" | grep -q "uvicorn" && echo "$PACKAGES_LIST" | grep -q "pymongo" && echo "$PACKAGES_LIST" | grep -q "pydantic"; then
    echo "✅ Core dependencies already installed"
    
    # Check if requirements.txt has newer versions
    DRY_RUN_OUTPUT=$(pip install --dry-run -r requirements.txt 2>/dev/null || echo "")
    if echo "$DRY_RUN_OUTPUT" | grep -q "would install\|would upgrade"; then
        echo "📦 Some packages need updating..."
        pip install -r requirements.txt
    else
        echo "✅ All dependencies are up to date"
    fi
else
    echo "📚 Installing dependencies..."
    pip install -r requirements.txt
fi

# Verify installation
echo "🔍 Verifying installation..."
echo "Python version: $(python3 --version)"
echo "Pip version: $(pip --version)"
echo ""
echo "📦 Installed packages:"
pip list | grep -E "(fastapi|uvicorn|pymongo|motor|pydantic|bcrypt|jose)"

echo ""
echo "🎉 Setup complete! Your TodoApp backend is ready!"
echo ""
echo "📋 Available commands:"
echo "1. Start server: uvicorn main:app --reload --host 0.0.0.0 --port 8000"
echo "2. Test API: python test_api.py"
echo "3. View docs: http://localhost:8000/docs"
echo "4. Test OAuth2: python test_oauth2.py"
echo "5. Deactivate venv: deactivate"
echo ""

# Check if server is already running
if lsof -Pi :8000 -sTCP:LISTEN -t >/dev/null 2>&1; then
    echo "⚠️  Server is already running on port 8000"
    echo "📖 API Documentation: http://localhost:8000/docs"
    echo "🔍 Health Check: http://localhost:8000/health"
    echo ""
    if [ "$AUTO_START" = true ]; then
        echo "🔄 Auto-restart enabled via flag. Restarting server..."
        pkill -f "uvicorn.*main:app" || true
        sleep 2
        START_SERVER=true
    else
        read -p "🔄 Do you want to restart the server? (y/n): " -n 1 -r
        echo
        if [[ $REPLY =~ ^[Yy]$ ]]; then
            echo "🛑 Stopping existing server..."
            pkill -f "uvicorn.*main:app" || true
            sleep 2
            START_SERVER=true
        else
            START_SERVER=false
        fi
    fi
else
    if [ "$AUTO_START" = true ]; then
        START_SERVER=true
    else
        read -p "🚀 Do you want to start the server now? (y/n): " -n 1 -r
        echo
        if [[ $REPLY =~ ^[Yy]$ ]]; then
            START_SERVER=true
        else
            START_SERVER=false
        fi
    fi
fi

if [ "$START_SERVER" = true ]; then
    echo "🌟 Starting TodoApp backend server..."
    echo "📖 API Documentation will be available at: http://localhost:8000/docs"
    echo "🔐 OAuth2 Authentication: Username: test@example.com, Password: testpassword123"
    echo "💡 Press Ctrl+C to stop the server"
    echo ""
    
    # Start the server with proper environment
    export PYTHONPATH="${SCRIPT_DIR}:${PYTHONPATH:-}"
    
    # Try uvicorn with python module approach
    echo "🔧 Starting server..."
    python3 -m uvicorn main:app --reload --host 0.0.0.0 --port 8000
else
    echo "✅ Setup complete! Run the server manually when ready."
    echo "💡 Use: uvicorn main:app --reload --host 0.0.0.0 --port 8000"
fi
