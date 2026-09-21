from fastapi import FastAPI
from commands.actions import ApplicationSubmissionCommand
from commands.bus import CommandBus
from handlers.application import ApplicationSubmissionHandler
from repositories.in_memory import InMemoryRepository
from schemas import ApplicationSubmission
from starlette.status import HTTP_200_OK

repository = InMemoryRepository[ApplicationSubmissionCommand]()
command_bus = CommandBus()
command_bus.register(
    ApplicationSubmissionCommand, ApplicationSubmissionHandler(repository)
)

app = FastAPI()


@app.post("/application", response_model=ApplicationSubmission, status_code=HTTP_200_OK)
def create_application(application: ApplicationSubmission) -> ApplicationSubmission:
    command = ApplicationSubmissionCommand(**application.model_dump())
    return command_bus.dispatch(command)
