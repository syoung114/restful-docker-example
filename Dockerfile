#Template file

# Base image
FROM ubuntu:latest

# Update package lists
RUN apt-get update

# Install necessary packages
#RUN apt-get install -y <package-name1> <package-name2>

# Copy application files into the container
#COPY . /app

# Set the working directory to /app
#WORKDIR /app

# Expose port for the application
#EXPOSE <port>

# Define entrypoint command
CMD [ "python", "./app.py" ]
