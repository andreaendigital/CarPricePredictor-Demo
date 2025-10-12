FROM python:3.11-slim

WORKDIR /app

# Copy pyproject.toml from parent directory and install dependencies
COPY ../pyproject.toml .
RUN pip install --no-cache-dir -e .[frontend]

# Copy frontend code (current directory since context is ./frontend)
COPY . .

EXPOSE 3000

CMD ["python", "app.py"]
