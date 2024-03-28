# Use the official Python image as a base image
FROM python:3.8-slim

# Install required packages
RUN pip install selenium

# Set the working directory
WORKDIR /app

# Copy your Selenium WebDriver script into the container
COPY your_script.py .

# Define the command to execute your script
CMD ["python", "your_script.py"]