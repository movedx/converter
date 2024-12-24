# Use the official Python image from the Docker Hub
FROM python:3.13-slim

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE converter.settings

# Set the working directory
WORKDIR /app

# Install ffmpeg
RUN apt-get update && apt-get install -y ffmpeg

# Copy the requirements file into the container
COPY requirements.txt /app/

# Install the dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Copy the rest of the application code into the container
COPY . /app/

# Expose the port the app runs on
EXPOSE 8123

# Collect static files
RUN python manage.py collectstatic --noinput

# Run database migrations
RUN python manage.py migrate

# Create a directory for media files
RUN mkdir -p /app/media/uploads

# Set the entrypoint to run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8123"]