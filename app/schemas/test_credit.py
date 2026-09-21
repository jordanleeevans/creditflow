import pytest
from pydantic import ValidationError
from schemas import ApplicationSubmission


def test_credit_rating_success():
    try:
        ApplicationSubmission(id=1, name="John Doe", credit_rating=50, homeowner=True)
    except ValidationError:
        pytest.fail("Expected a valid schema.")


def test_credit_rating_failure():
    with pytest.raises(ValidationError):
        ApplicationSubmission(
            id=1, name="Jane Doe", credit_rating=1001, homeowner=False
        )
