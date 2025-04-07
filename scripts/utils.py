"""
Utility functions for the project are defined here
"""
from pydantic import BaseModel
from typing import Optional
from datetime import date
from classes import case
from classes import law_firm    
from classes import intake_form

#Law Firm object (many more fields to be added later)
class LawFirm():

    def __init__(self, email: str, firm_name: str, location: str, size: str):
        self.email = email
        self.firm_name = firm_name
        self.location = location
        self.size = size

    def get_firm_name(self):
        return self.firm_name
    
    def get_self_location(self):
        return self.location
    
    def get_size(self):
        return self.size
    
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
    