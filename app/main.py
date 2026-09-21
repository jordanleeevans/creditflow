from fastapi import FastAPI
from schemas import ApplicationSubmission
from starlette.status import HTTP_200_OK

app = FastAPI()


@app.post("/application", response_model=ApplicationSubmission, status_code=HTTP_200_OK)
def create_application(application: ApplicationSubmission):
    return application
