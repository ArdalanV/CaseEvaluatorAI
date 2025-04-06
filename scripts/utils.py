"""
Utility functions for the project are defined here
"""
from pydantic import BaseModel
from typing import Optional
from datetime import date

class IntakeFormRequest(BaseModel):
    name: str
    age: int
    injured: bool
    insured: bool
    liabilities:str
    injuries: str
    injury_type: str
    incident_date: date
    location: str
    story: str

class Intake_Form():

    def __init__(self, name, age, injured,insured, liabilities, injuries, injury_type, incident_date, location, story):
        self.name = name
        self.age = age
        self.injured = injured
        self.insured = insured
        self.liabilities = liabilities
        self.injuries = injuries
        self.injury_type = injury_type
        self.incident_date = incident_date
        self.location = location
        self.story = story

    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age

    def is_injured(self):
        return self.injured
    
    def is_insured(self):
        return self.insured
    
    def get_liabilities(self):
        return self.liabilities
    
    def get_injuries(self):
        return self.injuries
    
    def get_injury_type(self):
        return self.injury_type

    def get_incident_date(self):
        return self.incident_date
    
    def get_location(self):
        return self.location
    
    def get_story(self):
        return self.story
    
class Case():

    def __init__(self, first_name: str, last_name: str, email: str, phone_num: str,
                  case_description: str):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_num = phone_num
        self.case_description = case_description

    def get_first_name(self):
        return self.first_name
    
    def get_last_name(self):
        return self.last_name
    
    def get_email(self):
        return self.email
    
    def get_phone_num(self):
        return self.phone_num
    
    def get_case_description(self):
        return self.case_description
    

    
def make_intake_form(form: IntakeFormRequest):
    """
    A function for processing the intake form that the user filled out on the 
    web application

    Parameters:
        form (IntakeFormRequest): The form that needs to be converted to intake form object
    
    Returns:
        intake (Intake_Form): Returns an intake form
    """
    intake = Intake_Form(**form.model_dump())
    return intake
    