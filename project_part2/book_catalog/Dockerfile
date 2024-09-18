# Dockerfile for book_catalog microservice
# Dockerfile for book_catalog microservice
# Using the official Python slim image
FROM python:3.9-slim

# Setting the working directory inside the container
WORKDIR /app

# Copy requirements.txt file into the container
COPY requirements.txt .

# Install the Python dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project folder into the container
COPY . .

# Expose the port the FastAPI app will run on
EXPOSE 8000

# Command to run the FastAPI app using Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
