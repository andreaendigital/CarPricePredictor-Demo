.PHONY: help dev dev-python dev-docker run-dev test setup docs docs-serve docs-build docs-deploy clean pre-commit setup-legacy test-migration

help:
	@echo "Car Price Prediction Platform - Unified Development"
	@echo "Available commands:"
	@echo "  setup       -  Modern setup (pyproject.toml)"
	@echo "  dev         -  Smart launcher (interactive choice)"
	@echo "  dev-python  -  Python development (start-local.sh)"
	@echo "  dev-docker  -  Docker development (docker-compose)"
	@echo "  test        -  Run full test suite"
	@echo "  docs        -  Documentation development server"
	@echo "  docs-build  -  Build documentation site"
	@echo "  docs-deploy -  Deploy docs to GitHub Pages"
	@echo "  clean       -  Clean build artifacts"
	@echo "  pre-commit  -  Run pre-commit on all files"
	@echo "  setup-legacy -  Legacy setup (requirements.txt)"
	@echo "  test-migration -  Test new pyproject.toml setup"
	@echo "  run-dev     -  Legacy docker command (deprecated)"

dev:
	@echo "Car Price Prediction Platform - Smart Launcher"
	@echo "================================================="
	@echo "Choose your development environment:"
	@echo "  1) 🐍 Python (Local services)"
	@echo "  2) 🐳 Docker (Containerized)"
	@echo "  3) ❌ Cancel"
	@read -p "Enter choice [1-3]: " choice; \
	case $$choice in \
		1) make dev-python ;; \
		2) make dev-docker ;; \
		3) echo "👋 Cancelled" ;; \
		*) echo "❌ Invalid choice" ;; \
	esac

dev-python:
	@echo "Starting Python Development Environment..."
	@echo "============================================="
	@echo "Running full test verification before startup..."
	@make test || (echo "❌ Tests failed - fix issues before starting" && exit 1)
	@echo "All tests passed - starting services..."
	@if [ ! -f "scripts/start-local.sh" ]; then \
		echo "❌ scripts/start-local.sh not found"; \
		exit 1; \
	fi
	@chmod +x scripts/start-local.sh
	@./scripts/start-local.sh

dev-docker:
	@echo "Starting Docker Development Environment..."
	@echo "============================================"
	@echo "Running full test verification before build..."
	@make test || (echo "❌ Tests failed - fix issues before building" && exit 1)
	@echo "All tests passed - building and starting containers..."
	@if ! command -v docker >/dev/null 2>&1; then \
		echo "❌ Docker not installed"; \
		exit 1; \
	fi
	@if [ ! -f "config/docker-compose.dev.yml" ]; then \
		echo "❌ config/docker-compose.dev.yml not found"; \
		exit 1; \
	fi
	@docker-compose -f config/docker-compose.dev.yml up -d
	@./scripts/docker-status.sh
	@docker-compose -f config/docker-compose.dev.yml logs -f

setup:
	@echo "Setting up Car Price Prediction Platform..."
	@echo "============================================="
	@echo "Checking Python..."
	@python3 --version || (echo "❌ Python3 not found" && exit 1)
	@echo "Checking pip..."
	@pip --version || (echo "❌ pip not found" && exit 1)
	@echo "Installing project with all dependencies (pyproject.toml)..."
	@pip install -e .[dev]
	@echo "Installing pre-commit hooks..."
	@pre-commit install --config config/.pre-commit-config.yaml
	@echo "Setup complete! Available commands:"
	@echo "   • make dev     - Start development environment"
	@echo "   • make test    - Run test suite"
	@echo "   • make docs    - Start documentation server"
	@echo "   • Pre-commit hooks active - quality checks on every commit"
	@echo "   • Modern pyproject.toml configuration active"


test:
	@echo "Running Full Test Suite..."
	@echo "============================="
	@echo "Backend Tests:"
	@cd backend && python3 -m pytest ../tests/test_backend.py -v --cov=. --cov-report=term-missing
	@echo "\nFrontend Tests:"
	@cd frontend && python3 -m pytest tests/ -v --cov=. --cov-report=term-missing
	@echo "\n🔗 Integration Tests:"
	@python3 -m pytest tests/test_integration.py -v
	@echo "\nAll tests completed!"

docs:
	@echo "Starting Documentation Development Server..."
	@echo "============================================="
	@if ! command -v mkdocs >/dev/null 2>&1; then \
		echo "Installing MkDocs..."; \
		pip install mkdocs-material mkdocs-git-revision-date-localized-plugin pymdown-extensions; \
	fi
	@echo "🌐 Documentation server: http://localhost:8000"
	@echo "🔄 Auto-reload enabled for live editing"
	@cp config/mkdocs.yml ./mkdocs-temp.yml && mkdocs serve --config-file mkdocs-temp.yml; rm -f mkdocs-temp.yml

docs-build:
	@echo "📝 Building Documentation Site..."
	@echo "=============================="
	@if ! command -v mkdocs >/dev/null 2>&1; then \
		echo "📦 Installing MkDocs..."; \
		pip install mkdocs-material mkdocs-git-revision-date-localized-plugin pymdown-extensions; \
	fi
	@cp config/mkdocs.yml ./mkdocs-temp.yml && mkdocs build --clean --strict --config-file mkdocs-temp.yml && rm -f mkdocs-temp.yml
	@echo "✅ Documentation built in ./site directory"

docs-deploy:
	@echo "🚀 Deploying Documentation to GitHub Pages..."
	@echo "============================================="
	@if ! command -v mkdocs >/dev/null 2>&1; then \
		echo "📦 Installing MkDocs..."; \
		pip install mkdocs-material mkdocs-git-revision-date-localized-plugin pymdown-extensions; \
	fi
	@echo "⚠️  This will deploy to GitHub Pages"
	@read -p "Continue? [y/N]: " confirm; \
	if [ "$$confirm" = "y" ] || [ "$$confirm" = "Y" ]; then \
		mkdocs gh-deploy --clean --config-file config/mkdocs.yml; \
		echo "✅ Documentation deployed!"; \
	else \
		echo "👋 Deployment cancelled"; \
	fi

clean:
	@echo "🧹 Cleaning Build Artifacts..."
	@echo "============================"
	@echo "🗑️  Removing Python cache files..."
	@find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	@find . -name "*.pyc" -delete 2>/dev/null || true
	@find . -name "*.pyo" -delete 2>/dev/null || true
	@echo "🗑️  Removing test artifacts..."
	@rm -rf .pytest_cache/ .coverage htmlcov/ 2>/dev/null || true
	@echo "🗑️  Removing documentation build..."
	@rm -rf site/ 2>/dev/null || true
	@echo "🗑️  Removing project Docker containers..."
	@docker-compose -f config/docker-compose.dev.yml down 2>/dev/null || true
	@docker rmi p11-backend p11-frontend p11-docs carprice-backend 2>/dev/null || true
	@echo "✅ Cleanup completed!"

pre-commit:
	@echo "🔒 Running Pre-commit on All Files..."
	@echo "===================================="
	@if ! command -v pre-commit >/dev/null 2>&1; then \
		echo "📦 Installing pre-commit..."; \
		pip install pre-commit; \
		pre-commit install --config config/.pre-commit-config.yaml; \
	fi
	@pre-commit run --all-files --config config/.pre-commit-config.yaml
	@echo "✅ Pre-commit checks completed!"

setup-legacy:
	@echo "📦 Legacy Setup (requirements.txt files)..."
	@echo "==========================================="
	@echo "⚠️  Using legacy requirements.txt files"
	@echo "🔍 Checking Python..."
	@python3 --version || (echo "❌ Python3 not found" && exit 1)
	@echo "🔍 Checking pip..."
	@pip --version || (echo "❌ pip not found" && exit 1)
	@echo "📦 Installing backend dependencies..."
	@cd backend && pip install -r requirements.txt
	@echo "📦 Installing frontend dependencies..."
	@cd frontend && pip install -r requirements.txt
	@echo "🧪 Installing test dependencies..."
	@pip install pytest pytest-cov black flake8 requests
	@echo "📚 Installing documentation dependencies..."
	@pip install mkdocs-material mkdocs-git-revision-date-localized-plugin pymdown-extensions click
	@echo "🔒 Installing pre-commit hooks..."
	@pip install pre-commit
	@pre-commit install --config config/.pre-commit-config.yaml
	@echo "✅ Legacy setup complete!"

test-migration:
	@echo "🧪 Testing pyproject.toml Migration..."
	@echo "===================================="
	@echo "🔍 Validating pyproject.toml..."
	@python3 -c "import tomllib; f=open('pyproject.toml','rb'); tomllib.load(f); print('✅ pyproject.toml is valid')" 2>/dev/null || python3 -c "import tomli; f=open('pyproject.toml','rb'); tomli.load(f); print('✅ pyproject.toml is valid')" 2>/dev/null || echo "⚠️  Install tomli: pip install tomli"
	@echo "🚀 Testing new setup..."
	@pip install -e .[test] --quiet
	@echo "🧪 Running test suite..."
	@python3 -m pytest tests/test_backend.py -v --tb=short
	@echo "✅ Migration test completed successfully!"
