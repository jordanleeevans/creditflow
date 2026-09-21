from pydantic import BaseModel, PositiveInt, field_validator


class ApplicationSubmission(BaseModel):
    name: str
    credit_rating: PositiveInt
    homeowner: bool

    @field_validator("credit_rating")
    @classmethod
    def validate_credit_rating(cls, value: int) -> int:
        if value >= 1000:
            raise ValueError(
                "Credit rating must be a positive integer less than",
                " or equal to 1000.",
            )
        return value
