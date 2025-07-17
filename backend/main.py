# backend/main.py
from fastapi import FastAPI
from api.routes.test_cases import router as test_case_router

app = FastAPI()
app.include_router(test_case_router, prefix="/generate", tags=["Test Cases"])
