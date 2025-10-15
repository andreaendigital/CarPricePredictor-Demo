#!/bin/bash

echo ""
echo "🐳 Docker Services Status Check..."
echo "=================================="

# Wait for services to be ready
sleep 5

# Check if containers are running
BACKEND_STATUS=$(docker-compose -f config/docker-compose.dev.yml ps -q backend | wc -l)
DOCS_STATUS=$(docker-compose -f config/docker-compose.dev.yml ps -q docs | wc -l)
FRONTEND_STATUS=$(docker-compose -f config/docker-compose.dev.yml ps -q frontend | wc -l)

if [ "$BACKEND_STATUS" -eq 1 ] && [ "$DOCS_STATUS" -eq 1 ] && [ "$FRONTEND_STATUS" -eq 1 ]; then
    echo "✅ All services are running!"
    echo ""
    echo "🌐 Access Points:"
    echo "   • 🎨 Web Application: http://localhost:3000"
    echo "   • 🚀 Backend API: http://localhost:5002"
    echo "   • 📚 API Documentation: http://localhost:5004/docs-menu"
    echo "   • 📖 Swagger UI: http://localhost:5004/docs/"
    echo ""
    echo "🛠️  Development Commands:"
    echo "   • docker-compose -f config/docker-compose.dev.yml logs -f  - View logs"
    echo "   • docker-compose -f config/docker-compose.dev.yml down     - Stop services"
    echo "   • make test                                         - Run tests"
    echo ""
    echo "Press Ctrl+C to stop all services"
else
    echo "⚠️  Some services may not be ready yet. Check logs:"
    echo "   docker-compose -f config/docker-compose.dev.yml logs"
fi
