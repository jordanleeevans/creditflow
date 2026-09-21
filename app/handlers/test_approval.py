from commands.actions import ApplicationApprovalCommand
from handlers.approval import ApplicationApprovalHandler
from repositories.in_memory import InMemoryRepository
from schemas.credit import (
    ApplicationApproval,
    ApprovalDecision,
    RiskCategory,
)


def test_application_approval_handler_approves_low_risk_application():
    repo = InMemoryRepository[int, ApplicationApproval]()
    handler = ApplicationApprovalHandler(repo)
    command = ApplicationApprovalCommand(
        application_id=1,
        risk=RiskCategory.LOW,
    )

    result = handler.handle(command)

    assert result == ApplicationApproval(
        application_id=1,
        decision=ApprovalDecision.APPROVED,
    )
    assert repo.get(1) == result


def test_application_approval_handler_declines_high_risk_application():
    handler = ApplicationApprovalHandler()
    command = ApplicationApprovalCommand(
        application_id=1,
        risk=RiskCategory.HIGH,
    )

    result = handler.handle(command)

    assert result == ApplicationApproval(
        application_id=1,
        decision=ApprovalDecision.DECLINED,
    )
