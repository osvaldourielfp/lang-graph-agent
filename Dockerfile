# Use Python 3.11 slim image
FROM python:3.11-slim AS base

# Set working directory
WORKDIR /app

# Install system dependencies if needed (e.g., for graphviz)
RUN apt-get update && apt-get install -y graphviz && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY app/ ./app/

# Copy .env if it exists (for local builds)
COPY .env* ./

# Expose port if needed (uncomment if adding a web server)
# EXPOSE 8000

# Run the app
CMD ["python", "app/main.py"]
