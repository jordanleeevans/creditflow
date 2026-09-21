# CreditFlow

A small FastAPI service for assessing a credit application through a simple
command workflow:

1. submit the application
2. assess risk
3. decide approval

The HTTP layer stays thin. It passes the request into an application workflow,
and the workflow coordinates commands through a command bus.

## Architecture

```mermaid
flowchart TD
    Client[Client] --> API[POST /application]
    API --> Workflow[ApplicationWorkflow]

    Workflow --> SubmitCommand[ApplicationSubmissionCommand]
    Workflow --> RiskCommand[RiskAssessmentCommand]
    Workflow --> ApprovalCommand[ApplicationApprovalCommand]

    SubmitCommand --> Bus[CommandBus]
    RiskCommand --> Bus
    ApprovalCommand --> Bus

    Bus --> SubmitHandler[ApplicationSubmissionHandler]
    Bus --> RiskHandler[RiskAssessmentHandler]
    Bus --> ApprovalHandler[ApplicationApprovalHandler]

    SubmitHandler --> SubmissionRepo[(Submission Repository)]
    RiskHandler --> AssessmentRepo[(Risk Assessment Repository)]
    ApprovalHandler --> ApprovalRepo[(Approval Repository)]

    SubmitHandler --> Submission[ApplicationSubmission]
    RiskHandler --> Assessment[ApplicationRiskAssessment]
    ApprovalHandler --> Approval[ApplicationApproval]

    Approval --> API
```

## Project Layout

- `app/main.py`: FastAPI entrypoint and route definition.
- `app/workflows/`: application-level orchestration.
- `app/commands/`: command models and command bus.
- `app/handlers/`: command handlers for submission, risk, and approval.
- `app/repositories/`: in-memory repository abstraction.
- `app/schemas/`: request and response schemas.
- `app/logging_config.py`: structured JSON logging setup.

## Development

Run tests:

```bash
uv run pytest
```

Run the type checker:

```bash
uv run pyright app
```
