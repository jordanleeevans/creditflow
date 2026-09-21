from commands.actions import ApplicationApprovalCommand
from handlers.base import Handler
from repositories.base import Repository
from repositories.in_memory import InMemoryRepository
from schemas.credit import ApplicationApproval, ApprovalDecision, RiskCategory


class ApplicationApprovalHandler(Handler[ApplicationApprovalCommand]):
    def __init__(
        self, repo: Repository[int, ApplicationApproval] | None = None
    ) -> None:
        self.repo = repo or InMemoryRepository[int, ApplicationApproval]()

    def handle(self, command: ApplicationApprovalCommand) -> ApplicationApproval:
        decision = (
            ApprovalDecision.APPROVED
            if command.risk == RiskCategory.LOW
            else ApprovalDecision.DECLINED
        )
        approval = ApplicationApproval(
            application_id=command.application_id,
            decision=decision,
        )
        return self.repo.save(command.application_id, approval)

    def type(self) -> str:
        return "ApplicationApprovalHandler"
