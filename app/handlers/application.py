from commands.actions import ApplicationSubmissionCommand
from handlers.base import Handler
from repositories.in_memory import InMemoryRepository
from repositories.base import Repository
from schemas.credit import ApplicationSubmission


class ApplicationSubmissionHandler(Handler[ApplicationSubmissionCommand]):
    def __init__(
        self, repo: Repository[ApplicationSubmissionCommand] | None = None
    ) -> None:
        self.repo = repo or InMemoryRepository[ApplicationSubmissionCommand]()

    def handle(self, command: ApplicationSubmissionCommand) -> ApplicationSubmission:
        data = self.repo.save(command)
        return ApplicationSubmission(
            id=data.id,
            name=data.name,
            credit_rating=data.credit_rating,
            homeowner=data.homeowner,
        )

    def type(self) -> str:
        return "ApplicationSubmissionHandler"
