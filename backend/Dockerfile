FROM python:3.11-slim

WORKDIR /app

# Copy pyproject.toml from root and install dependencies
COPY pyproject.toml .
RUN pip install --no-cache-dir -e .[backend]

# Copy backend code
COPY backend/ .

EXPOSE 5002

CMD ["python", "app.py"]
