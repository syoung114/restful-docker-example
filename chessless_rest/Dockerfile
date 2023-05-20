#Template file

# Base image
FROM python:latest

WORKDIR /move_server
# Update package lists
#RUN apt-get update

# Install necessary packages
#RUN apt-get install -y <package-name1> <package-name2>

# Copy application files into the container
COPY chessless/Stockfish chessless/src/undaemonize.py move_server/move_server.py requirements.txt .

# Set the working directory to /app

# Expose port for the application
#EXPOSE <port>

# Define entrypoint command
RUN pip install requirements.txt

CMD [ "python", "-m", "flask", "run", "--host=0.0.0.0" ]
