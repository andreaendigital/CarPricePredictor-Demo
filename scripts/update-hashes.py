#!/usr/bin/env python3
"""
Auto-update pyproject.toml with SHA256 hashes
Usage: python scripts/update-hashes.py
"""
import subprocess
import sys
from pathlib import Path

def update_pyproject_with_hashes():
    """Generate requirements.txt with hashes, then update pyproject.toml"""
    print("🔄 Generating hashed requirements...")

    try:
        # Generate requirements.txt with hashes
        subprocess.run([
            "pip-compile",
            "--generate-hashes",
            "--extra=backend",
            "--extra=frontend",
            "--extra=test",
            "pyproject.toml"
        ], check=True)

        print("✅ Generated requirements.txt with SHA256 hashes")
        print("📋 Use: pip install -r requirements.txt (for production)")
        print("🚀 Use: pip install -e .[dev] (for development)")

    except subprocess.CalledProcessError as e:
        print(f"❌ Error: {e}")
        print("💡 Make sure pip-tools is installed: pip install pip-tools")
        sys.exit(1)
    except FileNotFoundError:
        print("❌ Error: pip-compile not found")
        print("💡 Install pip-tools: pip install pip-tools")
        sys.exit(1)

if __name__ == "__main__":
    update_pyproject_with_hashes()
