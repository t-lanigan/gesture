# Use an official lightweight Python image
FROM python:3.13.2-slim-bookworm

# Set the working directory inside the container
WORKDIR /app

# Copy necessary files
COPY requirements.txt ./
COPY ./config ./
COPY main.py ./
COPY controllers/ controllers/
COPY gestures/ gestures/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose ports (if needed)
EXPOSE 5000

# Default command to run the application
CMD ["python", "main.py"]