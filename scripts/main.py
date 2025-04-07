"""
API entry point for application
"""
import utils
from run import run
from fastapi import FastAPI

app = FastAPI()

@app.post("/intake")
def intake_endpoint(form: utils.IntakeFormRequest):
    #Creating Intake Form object
    intake_form = utils.make_intake_form(form)
    #Email created from intake form to be sent to law firm
    email = run(intake_form)

#Need to look up law firm email in database, send email to the firm (could be mobile app notification)
    
    

