# Set arguments
ARG BASE_CONTAINER=python:3.8

# Set the base image. 
FROM --platform=linux/amd64 $BASE_CONTAINER

# Adds metadata to image.
LABEL maintainer="Fernando"

# Sets the user name to use when running the image.
USER root
RUN apt-get update && apt-get install -y && apt-get clean

# Make a directory for our app
WORKDIR /producer

# Install dependencies
COPY requirements.txt .
COPY app.py .

RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy source code
COPY ./api ./api

# Run the application
CMD ["python", "-m", "api"]