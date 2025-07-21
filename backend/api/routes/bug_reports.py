from fastapi import APIRouter
from models.bug_report import BugReportRequest, BugReportResponse
from services.bug_report import generate_bug_report


router = APIRouter()

@router.post("/bug-reports", response_model=BugReportResponse)
def gerar_bug_report(request: BugReportRequest):
    bug_report = generate_bug_report(request.bug_description)
    return {"bug_report": bug_report}  # <- agora batendo com o model

