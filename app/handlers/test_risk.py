from commands.actions import RiskAssessmentCommand
from handlers.risk import RiskAssessmentHandler
from repositories.in_memory import InMemoryRepository
from schemas.credit import ApplicationRiskAssessment, RiskCategory


def test_risk_assessment_handler_returns_low_risk_for_strong_application():
    repo = InMemoryRepository[int, ApplicationRiskAssessment]()
    handler = RiskAssessmentHandler(repo)
    command = RiskAssessmentCommand(
        application_id=1,
        credit_rating=800,
        homeowner=True,
    )

    result = handler.handle(command)

    assert result == ApplicationRiskAssessment(
        application_id=1,
        risk=RiskCategory.LOW,
    )
    assert repo.get(1) == result


def test_risk_assessment_handler_returns_high_risk_for_weaker_application():
    handler = RiskAssessmentHandler()
    command = RiskAssessmentCommand(
        application_id=1,
        credit_rating=650,
        homeowner=True,
    )

    result = handler.handle(command)

    assert result == ApplicationRiskAssessment(
        application_id=1,
        risk=RiskCategory.HIGH,
    )
