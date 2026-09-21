from pydantic import BaseModel, ConfigDict, PositiveInt

from schemas.credit import RiskCategory


class Command(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")


class ApplicationSubmissionCommand(Command):
    id: PositiveInt
    name: str
    credit_rating: PositiveInt
    homeowner: bool


class RiskAssessmentCommand(Command):
    application_id: PositiveInt
    credit_rating: PositiveInt
    homeowner: bool


class ApplicationApprovalCommand(Command):
    application_id: PositiveInt
    risk: RiskCategory
