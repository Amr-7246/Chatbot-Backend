# Use official Python base image
FROM python:3.11-slim

# Set env to avoid buffering logs
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Copy requirements first
COPY requirements.txt .

# Optional: install OS dependencies for tools like uvicorn
RUN apt-get update && apt-get install -y build-essential

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY . .

# Expose FastAPI port
EXPOSE 8000

# Start the app
CMD ["uvicorn", "App.server:app", "--host", "0.0.0.0", "--port", "8000"]
