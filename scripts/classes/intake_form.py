from typing import List, Optional
from enum import IntEnum
from pydantic import BaseModel, Field, field_validator
from typing import Optional
from datetime import date

#Check if the person was injured, to design implementation to prompt uninjured claimant's elsewhere
# This will be used for better version of the intake form evalation process
# class IntakeFormBase(BaseModel):
#     first_name: str = Field(..., min_length=2, max_length=20, description='First name of the claimant')
#     last_name: str = Field(..., min_length=2, max_length=20, description='Last name of the claimant')
#     email: str = Field(..., min_length=3, max_length=50, description='Email of the claimant')
#     phone: str = Field(..., min_length=10, max_length=10, description='Phone number of the claimant')
#     injured: str = Field(..., min_length=2, max_length=3, description='Indicator if the claimant is injured')

#Intake Form Schema
class IntakeFormRequest(BaseModel):

    first_name: str = Field(..., min_length=2, max_length=20, description='First name of the claimant')
    last_name: str = Field(..., min_length=2, max_length=20, description='Last name of the claimant')
    email: str = Field(..., min_length=3, max_length=50, description='Email of the claimant')
    phone: str = Field(..., min_length=10, max_length=10, description='Phone number of the claimant')
    accident_type: str = Field(..., min_length=3, max_length=100, description='The type of accident the claimant was involved in')
    num_involved_people: int = Field(..., description='The number of people involved')
    is_injured: bool = Field(..., description='Indicator if the claimant is injured')
    injury_types: str = Field(..., min_length=3, max_length=512, description='The type of injuries the claimant has sustained')
    sought_medical_care: bool = Field(..., description='Indicator if the claimant sought medical care')
    filed_police_report: bool = Field(..., description='Indicator if the claimant filed a police report')
    is_insured: bool = Field(..., description='Indicator if the claimant is insured')
    insurance_coverage: str = Field(..., min_length=3, max_length=256, description='Type of insurance coverage the claimant possesses')
    has_witnesses: bool = Field(..., description='Indicator if the claimant has witnesses')
    incident_date: date = Field(..., 'The date of the incident')
    has_affordability_concerns: bool = Field(..., description='Indicator if the claimant has affordability concerns')
    city: str = Field(..., min_length=2, max_length=15, description='The city the incident occured in')
    state: str = Field(..., min_length=2, max_length=15, description='The state the incident occured in')
    medical_costs: Optional[str] = Field(None, description='The medical costs the claimant incurred')
    incident_description: str = Field(..., min_length=10, max_length=512, description='The claimants quick story of the incident')

    @field_validator('is_injured', 
               'sought_medical_care',
               'filed_police_report',
               'is_insured',
               'has_witnesses',
               'has_affordability_concerns',
               pre=True)
    def parse_booleans(cls, v):
        if isinstance(v, str):
            return v in ['yes', 'true', '1']
        return v

#Intake Form
class Intake_Form():

    def __init__(self, first_name: str, last_name: str, email: str, phone: str, accident_type: str, 
                 num_involved_people: int, is_injured: bool, injury_types: str, sought_medical_care: bool, 
                 filed_police_report: bool, is_insured: bool, insurance_coverage: str, has_witnesses: bool, 
                 incident_date: date, has_affordability_concerns: bool, city: str, state: str, 
                 incident_description: str, medical_costs=None):

        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.accident_type = accident_type
        self.num_involved_people = num_involved_people
        self.is_injured = is_injured
        self.injury_types = injury_types
        self.sought_medical_care = sought_medical_care
        self.filed_police_report = filed_police_report
        self.is_insured = is_insured 
        self.insurance_coverage = insurance_coverage
        self.has_witnesses = has_witnesses
        self.incident_date = incident_date
        self.has_affordability_concerns = has_affordability_concerns
        self.city = city
        self.state = state
        self.incident_description = incident_description
        self.medical_costs = medical_costs

    def get_first_name(self) -> str:
        return self.first_name

    def get_last_name(self) -> str:
        return self.last_name

    def get_email(self) -> str:
        return self.email
    
    def get_phone(self) -> str:
        return self.phone
    
    def get_accident_type(self) -> str:
        return self.accident_type
    
    def get_num_involved_people(self) -> int:
        return self.num_involved_people
    
    def get_is_injured(self) -> bool:
        return self.is_injured
    
    def get_injury_types(self) -> str:
        return self.injury_types

    def get_sought_medical_care(self) -> bool:
        return self.sought_medical_care

    def get_filed_police_report(self) -> bool:
        return self.filed_police_report

    def get_is_insured(self) -> bool:
        return self.is_insured
    
    def get_insurance_coverage(self) -> str:
        return self.insurance_coverage

    def get_has_witnesses(self) -> bool:
        return self.has_witnesses 
 
    def get_incident_date(self) -> date:
        return self.incident_date

    def get_has_affordability_concerns(self) -> bool:
        return self.has_affordability_concerns
     
    def get_city(self) -> str:
        return self.city
     
    def get_state(self) -> str:
        return self.state
    
    def get_incident_description(self) -> str:
        return self.incident_description
 
    def get_medical_costs(self) -> str:
        return self.medical_costs
    