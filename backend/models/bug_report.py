# backend/models/test_case.py
from pydantic import BaseModel
from typing import List, Optional

class BugReportRequest(BaseModel):
    bug_description: str

class BugReport(BaseModel):
    id: str
    title: str
    environment: str
    steps_to_reproduce: List[str]
    actual_result: str
    expected_result: str
    severity: str  # e.g., "Crítico", "Alto", "Médio", "Baixo"
    priority: str  # e.g., "Alta", "Média", "Baixa"
    evidence: Optional[str] = None  # print, log, descrição de erro
    notes: Optional[str] = None     # observações extras

class BugReportResponse(BaseModel):
    bug_report: BugReport
