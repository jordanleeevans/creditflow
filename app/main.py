from fastapi import FastAPI
from commands.actions import (
    ApplicationApprovalCommand,
    ApplicationSubmissionCommand,
    RiskAssessmentCommand,
)
from commands.bus import CommandBus
from handlers.approval import ApplicationApprovalHandler
from handlers.application import ApplicationSubmissionHandler
from handlers.risk import RiskAssessmentHandler
from repositories.in_memory import InMemoryRepository
from schemas import ApplicationApproval, ApplicationRiskAssessment, ApplicationSubmission
from starlette.status import HTTP_200_OK
from workflows.application import ApplicationWorkflow

repository = InMemoryRepository[int, ApplicationSubmissionCommand]()
assessment_repository = InMemoryRepository[int, ApplicationRiskAssessment]()
approval_repository = InMemoryRepository[int, ApplicationApproval]()
command_bus = CommandBus()
command_bus.register(
    ApplicationSubmissionCommand, ApplicationSubmissionHandler(repository)
)
command_bus.register(
    RiskAssessmentCommand, RiskAssessmentHandler(assessment_repository)
)
command_bus.register(
    ApplicationApprovalCommand, ApplicationApprovalHandler(approval_repository)
)
application_workflow = ApplicationWorkflow(command_bus)

app = FastAPI()


@app.post("/application", status_code=HTTP_200_OK)
def create_application(application: ApplicationSubmission) -> ApplicationApproval:
    return application_workflow.submit(application)
