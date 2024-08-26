# Use the official Python image from the Docker Hub
FROM python:3.12

# Set the working directory in the container
WORKDIR /workspace

# Install any necessary dependencies
RUN pip install --upgrade pip && \
    pip install black 

# Copy the current directory contents into the container at /workspace
COPY . /workspace

# Default command to run when starting the container
CMD ["bash"]
