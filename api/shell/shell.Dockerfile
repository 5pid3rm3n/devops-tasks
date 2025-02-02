FROM ubuntu:latest

# Update package list
RUN apt-get -y update

# Install curl
RUN apt-get install -y curl

WORKDIR /init-connector

# Copy all files to the container
COPY . .

# Make the initialization script executable
RUN chmod +x initialize-container.sh

# Run the initialization script
CMD ["/bin/bash", "initialize-container.sh"]