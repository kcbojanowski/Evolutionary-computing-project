# Use the official Python base image
FROM python:3.10

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

# Install the required dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Django project files to the container
COPY . .

# Set environment variables
ENV PYTHONUNBUFFERED=1

EXPOSE 8000

WORKDIR /app/oe2

# Run the Django development server
CMD ["/bin/bash","-c","./docker-init.sh"]