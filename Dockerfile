FROM python:3.13-slim

# Set the working directory inside the container
WORKDIR /app

# Prevent Python from writing bytecode files
ENV PYTHONDONTWRITEBYTECODE=1

# Display Python logs immediately
ENV PYTHONUNBUFFERED=1

# Install dependencies first to improve build caching
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy the application and tests into the container
COPY app/ ./app/

# Document the port used by the API
EXPOSE 8000

# Start the FastAPI application
CMD ["python", "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]