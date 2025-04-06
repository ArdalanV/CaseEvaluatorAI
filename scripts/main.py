"""
API entry point for application
"""
import utils
import run
from fastapi import FastAPI

app = FastAPI()

@app.post("/intake")
def intake_endpoint(form: utils.IntakeFormRequest):
    intake_form = utils.make_intake_form(form)
    processed_form = run.process_intake_form(intake_form)