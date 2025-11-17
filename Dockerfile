# Use Python 3.11 slim image
FROM python:3.11-slim AS base

# Set working directory
WORKDIR /app

# Install system dependencies if needed (e.g., for graphviz)
RUN apt-get update \
    && apt-get install -y --no-install-recommends graphviz curl ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Install uv package manager
RUN curl -LsSf https://astral.sh/uv/install.sh | sh -s -- --install-dir /usr/local/bin

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN uv pip install --system -r requirements.txt

# Copy app code
COPY app/ ./app/

# Copy .env if it exists (for local builds)
COPY .env* ./

COPY langgraph.json .

# Expose port if needed (uncomment if adding a web server)
# EXPOSE 8000

# # Run the app
# CMD ["python", "app/main.py"]
CMD ["langgraph", "dev"]