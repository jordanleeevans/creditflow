from fastapi import FastAPI
from commands.actions import ApplicationSubmissionCommand, RiskAssessmentCommand
from commands.bus import CommandBus
from handlers.application import ApplicationSubmissionHandler
from handlers.risk import RiskAssessmentHandler
from repositories.in_memory import InMemoryRepository
from schemas import ApplicationRiskAssessment, ApplicationSubmission
from starlette.status import HTTP_200_OK

repository = InMemoryRepository[int, ApplicationSubmissionCommand]()
assessment_repository = InMemoryRepository[int, ApplicationRiskAssessment]()
command_bus = CommandBus()
command_bus.register(
    ApplicationSubmissionCommand, ApplicationSubmissionHandler(repository)
)
command_bus.register(
    RiskAssessmentCommand, RiskAssessmentHandler(assessment_repository)
)

app = FastAPI()


@app.post("/application", status_code=HTTP_200_OK)
def create_application(application: ApplicationSubmission) -> ApplicationSubmission:
    command = ApplicationSubmissionCommand(**application.model_dump())
    return command_bus.dispatch(command)
