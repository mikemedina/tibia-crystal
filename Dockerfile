# Use a Linux base image
FROM ubuntu:latest

# Update the package lists and install necessary dependencies
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    sqlite3

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install the required packages
RUN pip3 install --no-cache-dir -r requirements.txt

# Install python-dotenv to handle .env or .flaskenv files
RUN pip3 install python-dotenv

# Copy the application code
COPY . .

# Run the database population script
RUN python3 populate_spells.py

# Expose the desired port
EXPOSE 5000

# Set the environment variables
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Run the application
CMD ["flask", "run"]

