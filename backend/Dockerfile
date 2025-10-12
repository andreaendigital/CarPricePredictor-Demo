FROM python:3.11-slim

WORKDIR /app

# Copy pyproject.toml from parent directory and install dependencies
COPY ../pyproject.toml .
RUN pip install --no-cache-dir -e .[backend]

# Copy backend code (current directory since context is ./backend)
COPY . .

EXPOSE 5002

CMD ["python", "app.py"]
