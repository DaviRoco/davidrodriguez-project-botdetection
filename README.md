# Docker Setup for the Bot Detection Project

This repository contains the Docker configuration to run this Bot Detection Project in isolated containers. Docker allows you to run your application with all its dependencies in a standardized environment, making it easier to manage development, testing, and deployment.

## Prerequisites

Make sure you have the following installed on your machine:

- **Docker**: [Download and install Docker](https://www.docker.com/get-started)
- **Docker Compose**: [Install Docker Compose](https://docs.docker.com/compose/install/)

## Project Structure

The project is set up with Docker Compose, which defines two services:

1. **App**: FastAPI application that connects to a PostgreSQL database.
2. **DB**: A PostgreSQL database used by the application.

## Setup and Running the Application

1. **Clone the repository**:

   ```bash
   git clone https://github.com/DaviRoco/davidrodriguez-project-botdetection.git
   cd davidrodriguez-project-botdetection
   
2. **Request .env file**

Request the .env file from other developers.


4. **Run Docker Containers**:
   ```bash
    docker-compose up --build
   
5. **Stop Containers**:
   ```bash
    docker-compose down
