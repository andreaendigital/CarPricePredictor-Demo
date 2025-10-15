FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy pyproject.toml from parent directory (context is ..)
COPY pyproject.toml .
RUN pip install --no-cache-dir -e .[backend]

# Copy backend code
COPY backend/ .

EXPOSE 5002

CMD ["python", "app.py"]
