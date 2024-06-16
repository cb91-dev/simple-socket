# Use the official Python image from the Docker Hub
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /workspace

# Copy the requirements file into the container
COPY app/requirements.txt /workspace/

# Install dependencies
RUN pip install --no-cache-dir -r /workspace/requirements.txt

# Copy the rest of the application code into the container
COPY app /workspace/app

# Set environment variable for Python path
ENV PYTHONPATH=/workspace

# Expose port for development
EXPOSE 8000

# Default command for the container
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
