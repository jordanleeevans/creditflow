import logging

from commands.actions import ApplicationSubmissionCommand
from handlers.base import Handler
from logging_config import log_extra
from repositories.in_memory import InMemoryRepository
from repositories.base import Repository
from schemas.credit import ApplicationSubmission

logger = logging.getLogger(__name__)


class ApplicationSubmissionHandler(Handler[ApplicationSubmissionCommand]):
    def __init__(
        self, repo: Repository[int, ApplicationSubmissionCommand] | None = None
    ) -> None:
        self.repo = repo or InMemoryRepository[int, ApplicationSubmissionCommand]()

    def handle(self, command: ApplicationSubmissionCommand) -> ApplicationSubmission:
        data = self.repo.save(command.id, command)
        logger.info(
            "Application submitted",
            **log_extra(
                event="application_submitted",
                application_id=command.id,
            ),
        )
        return ApplicationSubmission(
            id=data.id,
            name=data.name,
            credit_rating=data.credit_rating,
            homeowner=data.homeowner,
        )

    def type(self) -> str:
        return "ApplicationSubmissionHandler"
