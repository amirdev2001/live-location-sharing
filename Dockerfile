# Use Python image
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    binutils libproj-dev gdal-bin \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Collect static files
RUN python manage.py collectstatic --noinput

# Expose the application port
EXPOSE 8000

# Default command
CMD ["daphne", "-b", "0.0.0.0", "-p", "8000", "live_location_sharing_api.asgi:application"]
