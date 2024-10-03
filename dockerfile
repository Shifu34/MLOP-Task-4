# Dockerfile

# Use the official Python image from the Docker Hub
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file (if you have one) and install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port that Flask runs on
EXPOSE 5000

# Set the environment variable for Flask
ENV FLASK_APP=app.py

# Start the Flask application
CMD ["flask", "run", "--host=0.0.0.0"]
