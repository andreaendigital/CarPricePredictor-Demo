#!/bin/bash

echo "🚗 Car Price Prediction Platform - Development Status"
echo "===================================================="

# Check if services are running
check_service() {
    local url=$1
    local name=$2
    if curl -s "$url" > /dev/null 2>&1; then
        echo "✅ $name: Running ($url)"
    else
        echo "❌ $name: Not running ($url)"
    fi
}

echo "🔍 Checking services..."
check_service "http://localhost:5002/" "Backend API"
check_service "http://localhost:3000/" "Frontend Web"
check_service "http://localhost:5004/docs-menu" "API Documentation"

echo ""
echo "🌐 Access Points:"
echo "   • 🎨 Web Application: http://localhost:3000"
echo "   • 🚀 Backend API: http://localhost:5002"
echo "   • 📚 API Documentation: http://localhost:5004/docs-menu"
echo ""
echo "🛠️  Development Commands:"
echo "   • make dev         - Start development environment"
echo "   • make test        - Run full test suite"
echo "   • make setup       - One-time environment setup"
