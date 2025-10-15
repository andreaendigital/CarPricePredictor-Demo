FROM python:3.11-slim

WORKDIR /app

# Copy pyproject.toml and install dependencies
COPY pyproject.toml .
RUN pip install --no-cache-dir -e .[frontend]

# Copy frontend code
COPY frontend/ .

EXPOSE 3000

CMD ["python", "app.py"]
