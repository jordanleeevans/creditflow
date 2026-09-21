from fastapi import FastAPI
from fastapi import status

app = FastAPI()


@app.get("/application", status_code=status.HTTP_501_NOT_IMPLEMENTED)
def read_root():
    # TODO: Implement slim view that dispatches application submission to command bus
    return status.HTTP_501_NOT_IMPLEMENTED
