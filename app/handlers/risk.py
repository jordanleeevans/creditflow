import logging

from commands.actions import RiskAssessmentCommand
from handlers.base import Handler
from logging_config import log_extra
from repositories.base import Repository
from repositories.in_memory import InMemoryRepository
from schemas.credit import ApplicationRiskAssessment, RiskCategory

logger = logging.getLogger(__name__)


class RiskAssessmentHandler(Handler[RiskAssessmentCommand]):
    def __init__(
        self, repo: Repository[int, ApplicationRiskAssessment] | None = None
    ) -> None:
        self.repo = repo or InMemoryRepository[int, ApplicationRiskAssessment]()

    def handle(self, command: RiskAssessmentCommand) -> ApplicationRiskAssessment:
        risk = (
            RiskCategory.LOW
            if command.credit_rating >= 700 and command.homeowner
            else RiskCategory.HIGH
        )
        assessment = ApplicationRiskAssessment(
            application_id=command.application_id,
            risk=risk,
        )
        logger.info(
            "Application risk assessed",
            **log_extra(
                event="application_risk_assessed",
                application_id=command.application_id,
                risk=risk,
            ),
        )
        return self.repo.save(command.application_id, assessment)

    def type(self) -> str:
        return "RiskAssessmentHandler"
