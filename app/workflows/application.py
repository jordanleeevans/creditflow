import logging

from commands.actions import (
    ApplicationApprovalCommand,
    ApplicationSubmissionCommand,
    RiskAssessmentCommand,
)
from commands.bus import CommandBus
from logging_config import log_extra
from schemas.credit import ApplicationApproval, ApplicationSubmission

logger = logging.getLogger(__name__)


class ApplicationWorkflow:
    def __init__(self, command_bus: CommandBus) -> None:
        self.command_bus = command_bus

    def submit(self, application: ApplicationSubmission) -> ApplicationApproval:
        logger.info(
            "Application workflow started",
            **log_extra(
                event="application_workflow_started",
                application_id=application.id,
            ),
        )
        submission = self.command_bus.dispatch(
            ApplicationSubmissionCommand(**application.model_dump())
        )
        assessment = self.command_bus.dispatch(
            RiskAssessmentCommand(
                application_id=submission.id,
                credit_rating=submission.credit_rating,
                homeowner=submission.homeowner,
            )
        )
        approval = self.command_bus.dispatch(
            ApplicationApprovalCommand(
                application_id=assessment.application_id,
                risk=assessment.risk,
            )
        )
        logger.info(
            "Application workflow completed",
            **log_extra(
                event="application_workflow_completed",
                application_id=approval.application_id,
                decision=approval.decision,
            ),
        )
        return approval
