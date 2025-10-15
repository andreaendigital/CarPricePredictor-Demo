#!/bin/bash

echo "🚗 Car Price Prediction Platform - Python Development"
echo "===================================================="
echo "🔍 Running pre-flight checks..."

# Pre-flight checks
if ! command -v python3 >/dev/null 2>&1; then
    echo "❌ Python3 not found. Please install Python 3.9+"
    exit 1
fi

if ! command -v pip >/dev/null 2>&1; then
    echo "❌ pip not found. Please install pip"
    exit 1
fi

echo "✅ Python environment ready"

# Function to cleanup on exit
cleanup() {
    echo ""
    echo "🛑 Stopping services..."
    kill $BACKEND_PID $FRONTEND_PID $DOCS_PID 2>/dev/null
    exit 0
}

# Set trap to cleanup on Ctrl+C
trap cleanup SIGINT

# Install Dependencies from pyproject.toml
echo "📦 Installing Backend Dependencies..."
pip install -e ".[backend]"

echo "📦 Installing Frontend Dependencies..."
pip install -e ".[frontend]"

echo ""

# Start Backend API
echo "🚀 Starting Backend API (Port 5002)..."
cd backend
python3 app.py &
BACKEND_PID=$!
cd ..

# Wait a moment for backend to start
sleep 2

# Start Documentation Service
echo "📚 Starting Documentation Service (Port 5004)..."
cd backend
python3 app_swagger.py &
DOCS_PID=$!
cd ..

# Wait a moment for docs to start
sleep 2

# Start Frontend
echo "🎨 Starting Frontend Web Interface (Port 3000)..."
cd frontend
python3 app.py &
FRONTEND_PID=$!
cd ..

# Wait for services to initialize
sleep 3

echo ""
echo "✅ All services started successfully!"
echo ""
echo "🌐 Access Points:"
echo "   • 🎨 Web Application: http://localhost:3000"
echo "   • 🚀 Backend API: http://localhost:5002"
echo "   • 📚 API Documentation: http://localhost:5004/docs-menu"
echo "   • 📖 Swagger UI: http://localhost:5004/docs/"
echo "   • 📕 ReDoc: http://localhost:5004/redoc"
echo ""
echo "🛠️  Development Commands:"
echo "   • make test        - Run full test suite"
echo "   • make dev         - Restart development environment"
echo ""
echo "Press Ctrl+C to stop all services"
echo ""

# Keep script running
wait
