# Python API Monitoring Platform

A Python REST API built with FastAPI to simulate a service monitoring
platform.

## Features

- Application information endpoint
- Health-check endpoint
- Service listing
- Service details by ID
- Service health summary
- Application logging
- Error handling
- Automated tests

## Prerequisites

- Python
- Git
- FastAPI
- Uvicorn
- pytest
- HTTPX

## Run locally

Activate the Python virtual environment and run:

python -m uvicorn app.main:app --reload

## API documentation

http://127.0.0.1:8000/docs

## Run tests

python -m pytest -v