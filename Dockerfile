FROM python:3.9-slim

WORKDIR /app

# Copy requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code into container
COPY . .

# Expose port 5000 for REST API
EXPOSE 5000

# Start the application
CMD ["python", "app.py"]
