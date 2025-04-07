"""
Utility functions for the project are defined here
"""
from pydantic import BaseModel
from typing import Optional
from datetime import date

class IntakeFormRequest(BaseModel):
    first_name: str
    last_name: str
    email: str
    phone: str
    accident_type: str
    involved_people: str
    injured: str
    injury_types: str
    sought_medical_care: str
    filed_police_report: str
    insured: str
    witnesses: str
    incident_date: date
    affordability_costs: str
    city: str
    state: str
    country: str
    medical_costs: str
    incident_description: str

class Intake_Form():

    def __init__(self, first_name: str, last_name: str, email: str, phone: str, accident_type: str, 
                 involved_people: str, injured: str,injury_types: str, sought_medical_care: str, 
                 filed_police_report: str, insured: str, insurance_coverage: str, witnesses: str, incident_date: date, 
                 incident_description: str, affordability_concerns: str, city: str, state: str, 
                 country: str, medical_costs=None):

        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.accident_type = accident_type
        self.involved_people = involved_people
        self.injured = injured
        self.injury_types = injury_types
        self.sought_medical_care = sought_medical_care
        self.filed_police_report = filed_police_report
        self.insured = insured 
        self.insurance_coverage = insurance_coverage
        self.witnesses = witnesses
        self.incident_date = incident_date
        self.affordability_concerns = affordability_concerns
        self.city = city
        self.state = state
        self.country = country
        self.medical_costs = medical_costs
        self.incident_description = incident_description

    @property
    def get_first_name(self):
        return self.first_name

    @property
    def get_last_name(self):
        return self.last_name

    @property
    def get_email(self):
        return self.email
    
    @property
    def get_phone(self):
        return self.phone
    
    @property
    def get_accident_type(self):
        return self.accident_type
    
    @property
    def get_involved_people(self):
        return self.involved_people
    
    @property
    def is_injured(self):
        return self.injured
    
    @property
    def get_injury_types(self):
        return self.injury_types

    @property
    def has_sought_medical_care(self):
        return self.sought_medical_care

    @property
    def has_filed_police_report(self):
        return self.filed_police_report

    @property
    def is_insured(self):
        return self.insured
    
    @property
    def get_insurance_coverage(self):
        return self.insurance_coverage

    @property
    def has_witnesses(self):
        return self.witnesses 

    @property
    def get_incident_date(self):
        return self.incident_date

    @property
    def get_incident_description(self):
        return self.incident_description

    @property
    def has_affordability_concerns(self):
        return self.affordability_concerns
    
    @property
    def get_city(self):
        return self.city
    
    @property
    def get_state(self):
        return self.state
    
    @property
    def get_country(self):
        return self.country

    @property
    def get_medical_costs(self):
        return self.medical_costs

#Many fields to be added or changed
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

#Many more fields to be added later
class LawFirm():

    def __init__(self, email: str, firm_name: str, locations: list, size: str):
        self.email = email
        self.firm_name = firm_name
        self.locations = locations
        self.size = size

    def get_firm_name(self):
        return self.firm_name
    
    def get_self_location(self):
        return self.location
    
    def get_size(self):
        return self.size
    
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
    