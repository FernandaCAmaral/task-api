# Task API

Small REST API built with Python and FastAPI to practice backend basics.
I come from Java and Spring Boot and built this in two days to practice FastAPI.

## Endpoints
- GET /tasks: list tasks
- POST /tasks: create a task
- GET /tasks/{id}: get one task

## Run
pip install -r requirements.txt
uvicorn main:app --reload
Docs: http://127.0.0.1:8000/docs

## Test
pytest

## Next steps
Data is stored in memory. Next: PostgreSQL with SQLAlchemy.