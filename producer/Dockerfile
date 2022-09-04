FROM python:3.10-alpine

# Sets the user name to use when running the image.
USER root

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