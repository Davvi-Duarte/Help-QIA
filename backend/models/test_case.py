# backend/models/test_case.py
from pydantic import BaseModel
from typing import List

class TestCaseRequest(BaseModel):
    feature_description: str

class TestCase(BaseModel):
    id: str
    title: str
    steps: List[str]
    expected_result: str

class TestCaseResponse(BaseModel):
    test_cases: List[TestCase]
