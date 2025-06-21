FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy dependency list and install
COPY app/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire app folder contents into the container's /app directory
COPY app/ .

# Run the Flask application
CMD ["python", "app.py"]
