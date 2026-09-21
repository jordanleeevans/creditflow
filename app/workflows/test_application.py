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
from schemas.credit import (
    ApplicationApproval,
    ApplicationRiskAssessment,
    ApplicationSubmission,
    ApprovalDecision,
)
from workflows.application import ApplicationWorkflow


def test_application_workflow_submits_assesses_and_approves_application():
    command_bus = CommandBus()
    command_bus.register(
        ApplicationSubmissionCommand,
        ApplicationSubmissionHandler(
            InMemoryRepository[int, ApplicationSubmissionCommand]()
        ),
    )
    command_bus.register(
        RiskAssessmentCommand,
        RiskAssessmentHandler(InMemoryRepository[int, ApplicationRiskAssessment]()),
    )
    command_bus.register(
        ApplicationApprovalCommand,
        ApplicationApprovalHandler(InMemoryRepository[int, ApplicationApproval]()),
    )
    workflow = ApplicationWorkflow(command_bus)

    result = workflow.submit(
        ApplicationSubmission(
            id=1,
            name="John Doe",
            credit_rating=800,
            homeowner=True,
        )
    )

    assert result == ApplicationApproval(
        application_id=1,
        decision=ApprovalDecision.APPROVED,
    )
