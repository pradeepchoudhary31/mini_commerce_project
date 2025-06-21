# Dockerfile
FROM python:3.11-slim

# Set working directory
WORKDIR app

# Copy dependency list and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Run the Flask application
CMD ["python", "app.py"]