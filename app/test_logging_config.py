import json
import logging

from logging_config import JsonFormatter, log_extra


def test_json_formatter_includes_standard_and_extra_fields():
    formatter = JsonFormatter()
    record = logging.LogRecord(
        name="creditflow.test",
        level=logging.INFO,
        pathname=__file__,
        lineno=1,
        msg="Something happened",
        args=(),
        exc_info=None,
    )
    record.event = "application_submitted"
    record.application_id = 1

    payload = json.loads(formatter.format(record))

    assert payload["level"] == "INFO"
    assert payload["logger"] == "creditflow.test"
    assert payload["message"] == "Something happened"
    assert payload["event"] == "application_submitted"
    assert payload["application_id"] == 1
    assert "timestamp" in payload


def test_log_extra_wraps_fields_for_logger_extra_argument():
    assert log_extra(event="application_submitted", application_id=1) == {
        "extra": {
            "event": "application_submitted",
            "application_id": 1,
        }
    }
