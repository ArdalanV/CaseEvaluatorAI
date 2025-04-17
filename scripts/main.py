"""
API entry point for application
"""
from scripts import utils
from scripts.classes.intake_form import Intake_Form, IntakeFormRequest
from scripts import run
from fastapi import FastAPI

app = FastAPI()

#When the FrontEnd wants to create a new intake form
@app.post("/intake")
def create_intake_form(form: IntakeFormRequest):
    #Creating Intake Form object
    intake_form = utils.make_intake_form(form)
    #Email created from intake form to be sent to law firm
    run.first_phase(intake_form)
    return {"message": "Form processed successfully", 
            "intake_form": intake_form}

    
    

