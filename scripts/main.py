"""
API entry point for application
"""
import utils
import run
from fastapi import FastAPI

app = FastAPI()

@app.post("/intake")
def intake_endpoint(form: utils.IntakeFormRequest):
    result = run.process_intake_form(form)
    return result