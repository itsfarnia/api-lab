# API Lab

A simple FastAPI backend project for AI engineering practice.

This project demonstrates how to build basic API endpoints using Python, FastAPI, and Pydantic.

## What this project demonstrates

* FastAPI app setup
* GET endpoint
* POST endpoints
* Pydantic request models
* JSON request and response
* Basic error handling
* Simple AI-style backend logic

## Endpoints

### GET /health

Checks if the API is running.

### POST /summarize

Receives text and returns a simple summary.

### POST /classify

Receives text and classifies it into a simple category.

### POST /ask

Receives a question and returns a rule-based answer.

### POST /feedback

Receives user feedback and validates the rating.

## How to run

Install dependencies:

pip install -r requirements.txt

Run the API:

py -m uvicorn main:app --reload

Open the API docs:

http://127.0.0.1:8000/docs

## Example request

Endpoint:

POST /ask

Request body:

{
"question": "How can I get a refund?"
}

Example response:

{
"question": "How can I get a refund?",
"answer": "Customers can request a refund within 30 days of purchase."
}

## Project structure

api-lab/

* main.py
* requirements.txt
* .gitignore
* README.md

## How it works

1. The user sends a request to an endpoint.
2. FastAPI receives the request.
3. Pydantic checks the request body.
4. Python logic processes the input.
5. The API returns a JSON response.

## Limitations

This version does not use a real LLM.

The answers are rule-based.

There is no database yet.

There is no authentication.

## Future improvements

* Add OpenAI API
* Add environment variables
* Add database storage
* Add Dockerfile
* Add tests
