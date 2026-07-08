FROM python:3.10-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libhdf5-dev \
    libffi-dev \
    libssl-dev \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip and build tools
COPY requirements.txt .
RUN pip install --upgrade pip setuptools wheel
RUN pip install --no-cache-dir --upgrade pip setuptools wheel

# Install Python packages using PEP 517
RUN pip install --prefer-binary -r requirements.txt

# Copy the rest of the app
COPY . .

# Use the port that Render provides
EXPOSE $PORT
CMD ["sh", "-c", "streamlit run app/app.py --server.port=$PORT --server.address=0.0.0.0"]