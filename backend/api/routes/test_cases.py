# backend/api/routes/test_cases.py
from fastapi import APIRouter
from models.test_case import TestCaseRequest, TestCaseResponse
from services.test_case import generate_test_cases

router = APIRouter()

@router.post("/test-cases", response_model=TestCaseResponse)
def gerar_casos_de_teste(payload: TestCaseRequest):
    test_cases = generate_test_cases(payload.feature_description)
    return {"test_cases": test_cases}
