from commands.actions import (
    ApplicationApprovalCommand,
    ApplicationSubmissionCommand,
    RiskAssessmentCommand,
)
from commands.bus import CommandBus
from schemas.credit import ApplicationApproval, ApplicationSubmission


class ApplicationWorkflow:
    def __init__(self, command_bus: CommandBus) -> None:
        self.command_bus = command_bus

    def submit(self, application: ApplicationSubmission) -> ApplicationApproval:
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
        return self.command_bus.dispatch(
            ApplicationApprovalCommand(
                application_id=assessment.application_id,
                risk=assessment.risk,
            )
        )
