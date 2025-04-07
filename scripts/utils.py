"""
Utility functions for the project are defined here
"""
from pydantic import BaseModel
from typing import Optional
from datetime import date
from classes import case
from classes import law_firm    
from classes import intake_form

def make_intake_form(form: intake_form.IntakeFormRequest):
    """
    A function for processing the intake form that the user filled out on the 
    web application

    Parameters:
        form (IntakeFormRequest): The form that needs to be converted to intake form object
    
    Returns:
        intake (Intake_Form): Returns an intake form
    """
    intake = intake_form.Intake_Form(**form.model_dump())
    return intake
    