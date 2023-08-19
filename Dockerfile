# Use the official Python image as the base image
FROM python:3.8-slim-buster

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt requirements.txt

# Install dependencies
RUN pip install -r requirements.txt

# Copy the app files into the container
COPY . .

# Expose the port your Flask app will run on
EXPOSE 5000

# Command to run the app
CMD ["python", "src/app.py"]
