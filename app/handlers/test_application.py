from commands.actions import ApplicationSubmissionCommand
from handlers.application import ApplicationSubmissionHandler
from repositories.in_memory import InMemoryRepository
from schemas.credit import ApplicationSubmission


def test_application_submission_handler_saves_and_returns_submission():
    repo = InMemoryRepository[int, ApplicationSubmissionCommand]()
    handler = ApplicationSubmissionHandler(repo)
    command = ApplicationSubmissionCommand(
        id=1,
        name="John Doe",
        credit_rating=50,
        homeowner=True,
    )

    result = handler.handle(command)

    assert result == ApplicationSubmission(
        id=1,
        name="John Doe",
        credit_rating=50,
        homeowner=True,
    )
    assert repo.db[1] == command
