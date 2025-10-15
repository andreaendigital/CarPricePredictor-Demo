FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy pyproject.toml from parent directory (context is ..)
COPY pyproject.toml .
RUN pip install --no-cache-dir -e .[frontend]

# Copy frontend code
COPY frontend/ .

EXPOSE 3000

CMD ["python", "app.py"]
