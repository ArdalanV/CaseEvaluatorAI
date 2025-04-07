"""
API entry point for application
"""
import utils
from classes import case, intake_form, law_firm
from run import run
from fastapi import FastAPI

app = FastAPI()

#When the FrontEnd wants to create a new intake form
@app.post("/intake")
def create_intake_form(form: intake_form.IntakeFormRequest):
    #Creating Intake Form object
    intake_form = utils.make_intake_form(form)
    #Email created from intake form to be sent to law firm
    email = run(intake_form)

    
    

