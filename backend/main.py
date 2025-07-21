# backend/main.py
from fastapi import FastAPI
from api.routes.test_cases import router as test_case_router
from api.routes.bug_reports import router as bug_report_router

app = FastAPI()
app.include_router(test_case_router, prefix="/generate", tags=["Test Cases"])
app.include_router(bug_report_router, prefix="/generate", tags=["Bug Reports"])
