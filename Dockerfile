FROM python:3.8-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install dependencies in a virtual environment
RUN python -m venv venv && \
    . venv/bin/activate && \
    pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Install curl for healthcheck
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

# Set up a healthcheck
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:8000/health || exit 1

# Create a non-root user and switch to it
RUN adduser --disabled-password --gecos '' myuser
USER myuser

# Set environment variables
ENV PATH="/app/venv/bin:$PATH"

# Run the application
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "run:app"]
