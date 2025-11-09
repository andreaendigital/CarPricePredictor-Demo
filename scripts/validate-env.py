#!/usr/bin/env python3
"""Environment validation script for Car Price Predictor platform."""

import os
import sys
from pathlib import Path
from dotenv import load_dotenv

def validate_environment():
    """Validate that all required environment variables are properly configured."""

    # Load environment variables
    env_file = Path(__file__).parent.parent / ".env"
    if env_file.exists():
        load_dotenv(env_file)
        print(f"✅ Loaded environment from: {env_file}")
    else:
        print(f"⚠️  No .env file found at: {env_file}")
        print("   Using system environment variables only")

    # Required environment variables with their defaults
    required_vars = {
        "MODEL_PATH": "backend/modelo/modelo.joblib",
        "DB_PATH": "backend/vehiculos.json",
        "BACKEND_URL": "http://localhost:5002",
        "BACKEND_HOST": "0.0.0.0",
        "BACKEND_PORT": "5002",
        "FRONTEND_HOST": "0.0.0.0",
        "FRONTEND_PORT": "3000",
    }

    print("\n🔍 Environment Variable Validation:")
    print("=" * 50)

    all_valid = True

    for var, default in required_vars.items():
        value = os.getenv(var, default)
        status = "✅" if value else "❌"
        print(f"{status} {var:<20} = {value}")

        if not value:
            all_valid = False

    # Check file paths
    print("\n📁 File Path Validation:")
    print("=" * 50)

    model_path = Path(os.getenv("MODEL_PATH", "backend/modelo/modelo.joblib"))
    if model_path.exists():
        print(f"✅ ML Model found: {model_path}")
    else:
        print(f"⚠️  ML Model not found: {model_path}")
        print("   Application will use fallback prediction")

    db_path = Path(os.getenv("DB_PATH", "backend/vehiculos.json"))
    if db_path.exists():
        print(f"✅ Database file found: {db_path}")
    else:
        print(f"ℹ️  Database file will be created: {db_path}")

    # Check ports
    print("\n🌐 Port Configuration:")
    print("=" * 50)

    backend_port = os.getenv("BACKEND_PORT", "5002")
    frontend_port = os.getenv("FRONTEND_PORT", "3000")
    docs_port = os.getenv("DOCS_PORT", "5004")

    print(f"🔧 Backend API:     http://localhost:{backend_port}")
    print(f"🌐 Frontend Web:    http://localhost:{frontend_port}")
    print(f"📚 API Docs:        http://localhost:{docs_port}")

    # Summary
    print("\n📋 Environment Summary:")
    print("=" * 50)

    if all_valid:
        print("✅ All required environment variables are configured")
        print("🚀 Ready to start development environment")
        return True
    else:
        print("❌ Some environment variables are missing")
        print("💡 Check the .env file or set system environment variables")
        return False

if __name__ == "__main__":
    success = validate_environment()
    sys.exit(0 if success else 1)
