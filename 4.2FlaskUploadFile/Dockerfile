FROM python:3.10.11-slim-buster

WORKDIR /code

# Install required system dependencies
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install TensorFlow
RUN pip install --no-cache-dir tensorflow

# Copy your application code
COPY . /code

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Command to run your application
CMD ["flask", "run", "--host=0.0.0.0", "--port=8000"]
