from typing import List, Optional
from enum import IntEnum
from pydantic import BaseModel, Field
from typing import Optional
from datetime import date

#Intake Form Schema
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

#Intake Form
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

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_email(self):
        return self.email
    
    def get_phone(self):
        return self.phone
    
    def get_accident_type(self):
        return self.accident_type
    
    def get_involved_people(self):
        return self.involved_people
    
    def is_injured(self):
        return self.injured
    
    def get_injury_types(self):
        return self.injury_types

    def has_sought_medical_care(self):
        return self.sought_medical_care

    def has_filed_police_report(self):
        return self.filed_police_report

    def is_insured(self):
        return self.insured
    
    def get_insurance_coverage(self):
        return self.insurance_coverage

    def has_witnesses(self):
        return self.witnesses 
 
    def get_incident_date(self):
        return self.incident_date
 
    def get_incident_description(self):
        return self.incident_description

    def has_affordability_concerns(self):
        return self.affordability_concerns
     
    def get_city(self):
        return self.city
     
    def get_state(self):
        return self.state
      
    def get_country(self):
        return self.country
 
    def get_medical_costs(self):
        return self.medical_costs