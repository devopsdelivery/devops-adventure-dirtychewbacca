# app/Dockerfile

# Use the official Python image as the base image
FROM python:3.11-slim

# Install Poetry
RUN pip install poetry

# Set working directory
WORKDIR /app

# Copy the project files
COPY . /app

# Install project dependencies
RUN poetry install 

# Expose the port the app runs on
EXPOSE 8000


# Define environment variables 
ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=postgres
ENV POSTGRES_HOST=postgres 
ENV POSTGRES_DB=postgres

# Command to run when the container starts
CMD ["poetry", "run", "uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "8000"] 
# Este comando será OverRide pelo comando de RUN-APP do Makefile ou qualquer outra execução RUN da app


